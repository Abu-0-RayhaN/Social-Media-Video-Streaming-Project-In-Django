from django.contrib import admin

from.models import Category,Uploads,Like,Comment
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Uploads)
