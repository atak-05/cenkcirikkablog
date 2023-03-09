from django.shortcuts import render, get_object_or_404, redirect
from blog.models.text import textModel
from blog.forms.commentAdd import commentAddForm
from django.views import View
from django.contrib import messages
import logging 

logger = logging.getLogger('how_read_text')

class detailView(View):
    http_method_names= ['get', 'post']
    commentAddForm_ = commentAddForm
    
    def get(self, request,slug):
        text = get_object_or_404(textModel, slug=slug)
        if request.user.is_authenticated:
            logger.info( text.title+" " + "texti "+ request.user.username+" tarafından okundu!  ")
        comments = text.commentS.all()
        return render(request,'pages/detail.html', context={
        'text': text,
        'comments': comments,
        'addComment': self.commentAddForm_,
    })
        
    def post(self, request,slug):
        text = get_object_or_404(textModel, slug=slug)
        commentAddForm_ = self.commentAddForm_(data=request.POST)
        if commentAddForm_.is_valid():
            comment = commentAddForm_.save(commit=False)
            comment.author =request.user
            comment.text = text
            comment.save()   
            messages.success(request, "Comment added successfully")
        return redirect('detail', slug=slug)
 


    
