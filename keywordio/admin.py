from django.contrib import admin
from keywordio.models import *

# Register your models here.

admin.site.register(book)
admin.site.register(student)
admin.site.register(issuedbooks)
admin.site.register(studentissue)
class bookadmin(admin.ModelAdmin):
    list_display=['id','name','auther','ISBN','category','quantity']

class studentadmin(admin.ModelAdmin):
    list_display=['id','studentfirstname','studentlastname','branch','enrollnumber']

class issuedbooksadmin(admin.ModelAdmin):
    list_display=['id','studentname','bookname','branch','issueddate']
