from django.contrib.auth.decorators import login_required
from blog.models.comment import commentModel
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


@login_required(login_url='/')
def deleteComment(request,id):
    comment =  get_object_or_404(commentModel, id=id)
    if comment.author == request.user or comment.text.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted")
        return redirect('detail', slug= comment.text.slug)
    return redirect('home')