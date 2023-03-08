from django.db import models

class dataAbstractModel(models.Model):
    createdAtTime = models.DateTimeField(auto_now_add=True)
    updatedAtTime = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True #*soyut class herhangi bir tablo oluşturmaz sadece tekrar eden alanları eklediğimiz bir model.