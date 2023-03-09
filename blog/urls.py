from django.urls import path

from blog.views.contact import contactFormView
from blog.views.home import home
from blog.views.category import categoryListView
from blog.views.mytext import mytext
from blog.views.detail import detailView
from blog.views.addText import addTextCreateView
from blog.views.updateText import updateTextUpdateView
from blog.views.deleteText import deleteTextDeleteView
from blog.views.deleteComment import deleteComment
from django.views.generic import TemplateView, RedirectView
# * config/urls içerisinden gelen istediğin cevabı burada blog için
urlpatterns = [
    path('redirect', RedirectView.as_view(
        url = 'http://www.google.com'
        ), name='redirect'),
    path('', home, name='home'),
    path('about', TemplateView.as_view(
        template_name='pages/about.html'
        ) , name='about'),
    path('send-email', TemplateView.as_view(
        template_name='pages/send-email.html'
        ) , name='send-email'),
    path('contact' , contactFormView.as_view(), name='contact'),
    path('category/<slug:categorySlug>', categoryListView.as_view(), name='category'),
    path('mytext', mytext, name='mytext'),
    path('detail/<slug:slug>', detailView.as_view(), name='detail'),
    path('add-text',addTextCreateView.as_view(), name='addText'),
    path('update-text/<slug:slug>', updateTextUpdateView.as_view(), name='update-text'),
    path('delete-text/<slug:slug>', deleteTextDeleteView.as_view(), name='delete-text'),
    path('delete-comment/<int:id>', deleteComment, name='delete-comment'),

]
    
