from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import customUserModel
# Register your models here.

@admin.register(customUserModel) #*admin.site.register bu şekilde daha kolay yazılabilir.
class customAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Değiştirme Alanı', {
            'fields': ['avatar']
        }),
    ) #*burada yaptıgımız işlem useradmin içindeki fieldsetleri kullandık ve artı olarak avatar alanımızı oluşturduk!


# admin.site.register(customUserModel, customAdmin)