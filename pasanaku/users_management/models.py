from django.db import models

# Create your models here.
class UsersData(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class UserRoles(models.TextChoices):
    AD = 'ad', 'Admin'
    ST = 'st', 'Staff'
    NU = 'nu', 'Normal User'
    
class UsersLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(UsersData, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    user_role = models.CharField(max_length=2, choices=UserRoles.choices, default=UserRoles.NU)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    
