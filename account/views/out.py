from django.contrib.auth import logout
from django.shortcuts import redirect


def out(request): 
    logout(request)
    return redirect('home')