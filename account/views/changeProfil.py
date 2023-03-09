from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import changeProfilForm


@login_required(login_url='/')
def changeProfil(request):
    if request.method == 'POST':
        form = changeProfilForm(request.POST, request.FILES, instance = request.user) 
        if form.is_valid():
            form.save()
            messages.success(request,'Profil changed')
    else :
        form = changeProfilForm(instance = request.user)
    return render(request , 'pages/changeProfil.html', context ={
        'form':form 
    })