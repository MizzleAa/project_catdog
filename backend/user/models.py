from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class UserManage(BaseUserManager):
    def _create_user(self, username, password, role=None, **extra_fields):
        username = self.model.normalize_username(username)

        if extra_fields.get('is_admin') is True:
            role = self.get_role(id=1, role_name='Admin')
        else:
            role = self.get_role(id=2, role_name='User')

        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def get_role(self, id: int, role_name: str):
        role, _ = User_Role.objects.get_or_create(
            id=id,
            name=role_name
        )

        return role

    def create_user(self, username='', password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)

        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=20, primary_key=True, verbose_name='계정명')
    password = models.CharField(max_length=512, verbose_name='비밀번호')
    role = models.ForeignKey(
        'User_Role', on_delete=models.CASCADE, verbose_name='사용권한')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManage()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'User'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'


class User_Role(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'User_Role'
        verbose_name = '사용자 권한'
        verbose_name_plural = '사용자 권한'
