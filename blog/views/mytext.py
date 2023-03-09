from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#* urlsden gelen istediğin cevabı bu sayfada 

#* __init__.py sayfasına dahil etmeyi unutma!

@login_required(login_url='/')
def mytext(request):
    texts = request.user.texts.order_by('-id') #ters ilişki text model içerisindeki M2M sayesinde yaptık. #
    page = request.GET.get('page')
    paginator = Paginator(texts, 10)
    return render(request , 'pages/mytext.html', context={
        'texts': paginator.get_page(page),
        
    })
    


