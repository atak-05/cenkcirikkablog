from django.shortcuts import render, redirect
from blog.forms.textAdd import textAddForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from blog.models.text import textModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# m2m datası farklı bir yerde olduğu için onuda 
# -bu şekilde kayıt ediyoruz.
class addTextCreateView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    template_name='pages/addText.html'
    model = textModel
    fields = ['title','content','image','category']

    def get_success_url(self):
        return reverse('detail', kwargs={
            'slug' :self.object.slug
        })
    
    def form_valid(self, form):
        text = form.save(commit=False)
        text.author = self.request.user
        text.save()       
        form.save_m2m() 
        return super().form_valid(form)
        



#Create view kullanmazsak ---
# @login_required(login_url='/')
# def addText(request):
#     form = textAddForm(request.POST or None, files=request.FILES or None)
#     if form.is_valid():
#         text = form.save(commit=False)
#         text.author = request.user
#         text.save()       
#         form.save_m2m() 
#         return redirect('detail', slug= text.slug)
#     return render(request, 'pages/addText.html', context={
#         'form': form
#     })

