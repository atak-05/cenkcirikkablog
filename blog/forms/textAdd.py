from django import forms
from blog.models.text import textModel

class textAddForm(forms.ModelForm):
    class Meta:
        model = textModel
        exclude = ('author', 'slug')