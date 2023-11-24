from django.contrib import admin
from .models import Post,Topic,Comment

admin.site.register(Post)
# Register your models here.
admin.site.register(Topic)
admin.site.register(Comment)
