from django.views.generic import DetailView
from account.models import customUserModel
from django.shortcuts import get_object_or_404


class profileDetailView(DetailView):
    template_name = 'pages/profil.html'
    context_object_name = 'profil'
    
    def get_object(self):
        return get_object_or_404(
            customUserModel, username= self.kwargs.get('username')
        )