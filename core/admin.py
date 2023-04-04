from django.contrib import admin

from .models import Blog,Book,Author

@admin.register(Blog)
class BlAdm(admin.ModelAdmin):
    list_display=['title','body','created','updated']

@admin.register(Book)
class BooAdm(admin.ModelAdmin):
    list_display=['id','title','created','updated']

@admin.register(Author)
class AuthAdm(admin.ModelAdmin):
    list_display=['id','name','profession','created','updated']
