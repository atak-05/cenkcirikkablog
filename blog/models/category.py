from django.db import models
from autoslug import AutoSlugField


class categoryModel(models.Model):
    categoryName = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from= 'categoryName', unique=True)
    
    class Meta:
        db_table = 'category' 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.categoryName