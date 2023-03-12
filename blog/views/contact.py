from django.shortcuts import render, redirect
from blog.forms.contact import contactForm
from blog.models.contact import contactModel
from django.views.generic import FormView

#* __init__.py sayfasına dahil etmeyi unutma!
# def contact(request):
#     form = contactForm(
        # data= { #bunda ise bilgiler otomatik olarak gösteriliyor ama 
        # -onu gönderemiyor. Kendi bilgilerini doldurması gerekiyor.
        #     'name_lastname': 'Adınız ve Soyadınız',
        #     'email' : 'E-mail',
        #     'message' : 'Mesajım.',
        # }
        #Bu şekilde direk inputta değer atamış oluyoruz ve
        # kullanıcı otomatik bilgileri direk gönder diyebilir!
        # initial = {
        #     'name_lastname': 'Adınız ve Soyadınız',
        #     'email' : 'E-mail',
        #     'message' : 'Mesajım.',
        # }
    # )
    # if request.method == 'POST':
    #     form = contactForm(request.POST)
    #     print(form)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')

    # context = {
    #     'form': form
    # }
    # return render(request , 'pages/contact.html', context = context)

class contactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = contactForm
    success_url = 'send-email'
  
    
    def form_valid(self, form) :
        form.save()
        form.send_email(message=form.cleaned_data.get('message'))
        
        # return redirect(self.success_url)
        # aynı şey
        return super().form_valid(form)
    
    