from django.contrib import admin
from .models import UsersLogin, UsersData

# Register your models here.
admin.site.register(UsersLogin)
admin.site.register(UsersData)