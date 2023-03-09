from django.db import models
from autoslug import AutoSlugField
# from account.models import customUserModel #*kendi oluşturduğumuz user modeli kullanıyoruz.
from blog.models.category import categoryModel
from ckeditor.fields import RichTextField
from blog.abstractModel import dataAbstractModel



class textModel(dataAbstractModel):
    image = models.ImageField(upload_to='textImages')
    title = models.CharField(max_length=50)
    content = RichTextField()
    # createdAtTime = models.DateTimeField(auto_now_add=True)# bu sayede her oluşturulan yazı için otomatik tarih oluşturulacak..
    # updatedAtTime = models.DateTimeField(auto_now=True) #her değiştirildiğinde değiştirildiğindeki tarih olacaktır.
    slug = AutoSlugField(populate_from='title', unique=True)
    category = models.ManyToManyField(categoryModel, related_name='text')
    author =models.ForeignKey('account.customUserModel',related_name='texts',on_delete=models.CASCADE)
    # author = models.ForeignKey(customUserModel, related_name='texts',on_delete=models.CASCADE)
    #many_to_many: bir alanı başka bir tablonun birden fazla alan ile ilişkilendiriyor.
    #foreign_keys:bir tabloyu bir başka tablo ile ilişkilendirmesi sağlıyor.
    
    class Meta:
        verbose_name ='text'
        verbose_name_plural = 'Texts'
        db_table = 'text'
    def __str__(self):
        return self.title