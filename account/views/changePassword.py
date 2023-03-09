from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url='/')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user_ = form.save()
            update_session_auth_hash(request, user_)
            messages.success(request, "Password changed")
            return redirect('change-password')
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request , 'pages/changePassword.html', context ={
        'form' : form,
    })