from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
# from .forms import RegisterForm
from .models import User


class AIDMUserAdmin(admin.ModelAdmin):
    # add_form =RegisterForm
    model = User
    list_display = ('username',)

admin.site.register(User, AIDMUserAdmin)