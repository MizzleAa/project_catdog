from rest_framework import serializers, exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import User, User_Role


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password1 = serializers.CharField(max_length=512, write_only=True)
    password2 = serializers.CharField(
        max_length=512, write_only=True, label='password check')

    def validate(self, data):
        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'error': "Account Already Exists"})

        if password1 != password2:
            raise serializers.ValidationError(
                {'error': "The two password fields didn't match"})

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password1'],
            role=User_Role.objects.get_or_create(id=2, name='User')[0]
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=512, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is None:
            raise exceptions.AuthenticationFailed(
                {'error': 'User with given username and password does not exist'})
            # return {'username': 'None'}

        try:
            token = RefreshToken.for_user(user=user)

        except Exception as ex:
            raise serializers.ValidationError({'error': 'Failed create Token'})

        return {
            'username': user.username,
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        }


class ChangePWSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(
        max_length=512, label='current password', write_only=True, required=True)
    new_password1 = serializers.CharField(
        max_length=512, label='change password', write_only=True, required=True)
    new_password2 = serializers.CharField(
        max_length=512, label='change password check', write_only=True, required=True)

    def validate(self, data):
        if data.get('new_password1') != data.get('new_password2'):
            raise serializers.ValidationError(
                {'error': "New Password fields didn't match"})

        return data

    def validate_user(self, data):
        user = data['username']
        if not user.check_password(self.validated_data['old_password']):
            raise serializers.ValidationError(
                {'error': 'Old Password is not correct'})

        return data

    def save(self, data, **kwargs):
        user = data['username']

        user.set_password(self.validated_data['new_password1'])
        user.save()

        return {
            'username': str(user),
            'access_token': data['access_token']
        }


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=512)

    def validate(self, data):
        try:
            refresh_token = data['refresh_token']
            token = RefreshToken(refresh_token)
        except Exception as ex:
            raise exceptions.AuthenticationFailed({'error': "Invalid Token"})

        return token


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, data):
        try:
            refresh = RefreshToken(data['refresh_token'])
        except Exception as ex:
            raise serializers.ValidationError({'error': "Invalid Token"})

        data = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
