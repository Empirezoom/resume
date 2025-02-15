from django.contrib import admin
from . models import *


# Register your models here.


class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['id','c_name',]

class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','sur_name','first_name','last_name','email']

class CertificationAdmin(admin.ModelAdmin):
    list_display = ['id','school',]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','type','icon']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','subject','read','not_read']







admin.site.register(CompanyProfile,CompanyProfileAdmin) 
admin.site.register(About,AboutAdmin) 
admin.site.register(Certification,CertificationAdmin) 
admin.site.register(Category,CategoryAdmin) 
admin.site.register(Contact,ContactAdmin) 