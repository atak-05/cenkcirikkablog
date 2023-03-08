from django.db import models
from account.models import customUserModel #*kendi oluşturduğumuz user modelini kullanıyoruz..
from blog.models.text import textModel
from blog.abstractModel import dataAbstractModel

class commentModel(dataAbstractModel):
    author = models.ForeignKey(customUserModel , on_delete=models.CASCADE, related_name ='comment')    
    text = models.ForeignKey(textModel, on_delete=models.CASCADE, related_name='commentS') 
    comment = models.TextField()
    
    
    class Meta:
        db_table = 'comments'
        verbose_name ='comment'
        verbose_name_plural = 'comments'
    def __str__(self):
        return self.author.username
    