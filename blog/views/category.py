from django.shortcuts import render, get_object_or_404
# from blog.models import textModel
from django.core.paginator import Paginator
from blog.models.category import categoryModel
from django.views.generic import ListView


#* urlsden gelen istediğin cevabı bu sayfada 

#* __init__.py sayfasına dahil etmeyi unutma!


class categoryListView(ListView):
    template_name='pages/category.html'
    # context_object_name = 'texts' 
    # paginate_by = 2
    
    # def get_queryset(self):
    #     category = get_object_or_404(categoryModel,slug=self.kwargs['categorySlug'])
    #     return category.text.all().order_by('-id')  
    
