from django.db import models


class contactModel(models.Model):
    email = models.EmailField(max_length=255)
    name_lastname = models.CharField(max_length=155)
    message = models.TextField()
    createdAtTime = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'contact'
        verbose_name = 'contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return self.email

    