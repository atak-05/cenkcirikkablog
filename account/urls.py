from django.urls import path
from django.contrib.auth import views as auth_views
from account.views.out import out 
from account.views.changePassword import changePassword
from account.views.changeProfil import changeProfil
from account.views.profile import profileDetailView
from account.views.signIn import signIn

#as_view ile örnegin LoginView içindeki overrides edebiliyorz.
urlpatterns = [
    path('login',auth_views.LoginView.as_view(
        template_name='pages/login.html',
        ), name='login'),
    
    path ('out',out,name='out'),
    
    path('change-password', changePassword, name='change-password'),
    
    path('change-profil', changeProfil, name= 'change-profil'),
    
    path('sign-in', signIn, name= 'sign-in'),
    
    path('profile/<str:username>', profileDetailView.as_view(), name= 'profile')

]
