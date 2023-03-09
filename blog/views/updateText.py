from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import textUpdateForm
from blog.models.text import textModel
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class updateTextUpdateView(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    template_name= 'pages/updateText.html'
    fields = ('title', 'content', 'image', 'category')
    def get_object(self):
        text = get_object_or_404(
            textModel,
            slug = self.kwargs.get('slug'),
            author = self.request.user
        )
        return text
    def get_success_url(self):
        return reverse('detail', kwargs={
            'slug' : self.get_object().slug
        } )
        
        
  #UPDATE VİEW KULLANMASSAK BU ŞEKİLDE      
# m2m datası farklı bir yerde olduğu için onuda 
# -bu şekilde kayıt ediyoruz.
# @login_required(login_url='/')
# def updateText(request,slug):
#     text = get_object_or_404(textModel, slug=slug, author= request.user)
#     form = textUpdateForm(request.POST or None, files=request.FILES or None,
#             instance=text)
#     if form.is_valid():
#         form.save()
#         return redirect('detail', slug = text.slug)
#     return render(request, 'pages/updateText.html', context={
#         'form': form,
#     })