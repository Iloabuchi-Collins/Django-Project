from django.contrib import admin
from .models import Post

#  class Post(admin.ModelAdmin):
#      list_display = {
#          "title", "text", "author", "created_date", "published_date"
#      }


admin.site.register(Post)