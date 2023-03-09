from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import signInForm
from django.contrib.auth import login, authenticate

def signIn(request):
    if request.method == 'POST':
       form = signInForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=password)
           login(request, user)
           return redirect ('home')
           
    else :
        form = signInForm()

    return render(request , 'pages/signIn.html', context ={
        'form' : form,
    })