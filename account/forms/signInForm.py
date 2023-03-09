from django.contrib.auth.forms import UserCreationForm
from account.models import customUserModel


class signInForm(UserCreationForm):
    class Meta:
        model = customUserModel
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'avatar',
        )
