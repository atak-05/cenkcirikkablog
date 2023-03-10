from django import forms
from blog.models.contact import contactModel
from django.core.mail import send_mail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class contactForm(forms.ModelForm):
    class Meta:
        model = contactModel
        fields = ('name_lastname', 'email','message')
    

        
    def send_email(self,message):
        send_mail(
            subject='İletişim Formunda Yeni Mesaj Var',
            from_email=None,
            message=message,
            recipient_list=['gizemcirikka@outlook.com'],
            fail_silently=False
        )
        