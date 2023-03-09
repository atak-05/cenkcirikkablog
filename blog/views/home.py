from django.shortcuts import render
from blog.models.text import textModel
from django.core.paginator import Paginator
from django.db.models import Q
#* urlsden gelen istediğin cevabı bu sayfada 

#* __init__.py sayfasına dahil etmeyi unutma!

def home(request):
    query = request.GET.get('query')
    texts = textModel.objects.order_by('-id')
    if query:
        texts =texts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(texts, 3)
    return render(request , 'pages/home.html', context={
        'texts': paginator.get_page(page)
    })
    


