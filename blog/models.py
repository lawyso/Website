from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.conf import settings
from tinymce import HTMLField
User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author =models.ForeignKey(User,default=1,related_name='post_author',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = HTMLField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:details",kwargs={'pk':self.pk})

class Comment(models.Model):
    post =models.ForeignKey(Post,related_name='blog_comments',on_delete=models.CASCADE)
    comment =models.TextField()
    user = models.ForeignKey(User,related_name='user_comments',on_delete=models.CASCADE)
    timestamp =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.post.title,self.user)

    class Meta:
        verbose_name ='Comment'
        verbose_name_plural='Comments'
        ordering =['-timestamp']
