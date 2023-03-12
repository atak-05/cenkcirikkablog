from django import forms
from blog.models.contact import contactModel
from django.core.mail import send_mail
from crispy_forms.helper import FormHelper


class contactForm(forms.ModelForm):
    class Meta:
        model = contactModel
        fields = ('name_lastname', 'email','message')
        widgets = {
            'name_lastname':forms.TextInput(attrs={'placeholder': 'Name',}),
            'email':forms.TextInput(attrs={'placeholder': 'email'}),
            'message':forms.TextInput(attrs={'placeholder': 'message'}),
        }
    def __init__(self, *args, **kwargs):
        super(contactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
   
   
        
    def send_email(self,message):
        send_mail(
            subject='İletişim Formunda Yeni Mesaj Var',
            from_email=None,
            message=message,
            recipient_list=['gizemcirikka@outlook.com'],
            fail_silently=False
        )
        