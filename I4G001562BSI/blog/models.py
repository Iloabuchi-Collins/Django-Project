from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name = "Post"
        verbose_name_plural = "Post"
    title = models.CharField(max_length=200, help_text='Enter your post name')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(null=True)
    published_date = models.DateTimeField(null=True)

