from django.shortcuts import render
from .models import UsersLogin, UsersData

# Create your views here.
def users(request):
    items = UsersLogin.objects.values("username", "user_role", "is_deleted", "enabled").all()
    return render(request, 'users.html', {"users": items})

def userData(request):
    id_filter = request.GET.get("id")
    items = UsersData.objects.filter(id=id_filter)
    return render(request, 'userData.html', {"users": items})