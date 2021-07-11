from .decorators import AdminRequired, LoginRequired
from .serializers import CreateUserSerializer, LoginSerializer, ChangePWSerializer, LogoutSerializer, RefreshTokenSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            serializer.create(validated_data=user)

            return Response({
                'username': user['username'],
                'message': "Success"
            },
                status=status.HTTP_201_CREATED
            )

        return Response({'error': "Request Body Error"}, status=status.HTTP_409_CONFLICT)


# 모든 권한 허용
@permission_classes([AllowAny])
class LoginView(APIView):
    '''
    로그인
    '''

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        print(request)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data

            response = Response()
            response.set_cookie(
                key='access_token', value=user['access_token'], httponly=True)
            response.data = user
            response.status_code = status.HTTP_200_OK

            return response

        return Response({'error': "Request Body Error"}, status=status.HTTP_409_CONFLICT)


class UpdatePasswordView(APIView):
    permission_classes = [LoginRequired]
    authentication_classes = [JWTAuthentication]

    def get_object(self, queryset=None):
        user = self.request.user
        token = self.request.auth

        return {
            'username': user,
            'access_token': str(token)
        }

    def post(self, request, *args, **kwargs):
        serializer = ChangePWSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            object = self.get_object()
            if serializer.validate_user(object):
                data = serializer.save(object)
                response = Response()
                response.set_cookie(
                    key='access_token', value=data['access_token'], httponly=True)
                response.data = data
                response.status_code = status.HTTP_200_OK

                return response

        return Response({'error': "Request Body Error"}, status=status.HTTP_409_CONFLICT)


class LogoutView(APIView):
    permission_classes = [LoginRequired]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid(raise_exception=True):

            serializer.validated_data.blacklist()

            response = Response()
            response.delete_cookie('access_token')

            response.data = {
                'message': 'Success'
            }
            response.status_code = status.HTTP_200_OK

            return response

        return Response({'error': "Request Body Error"}, status=status.HTTP_409_CONFLICT)


class RefreshTokenView(APIView):
    permission_classes = [LoginRequired]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            token = serializer.validated_data

            response = Response()
            response.set_cookie(
                key='access_token', value=token['access_token'], httponly=True)
            response.data = token
            response.status_code = status.HTTP_201_CREATED

            return response

        return Response({'error': "Request Body Error"}, status=status.HTTP_409_CONFLICT)
