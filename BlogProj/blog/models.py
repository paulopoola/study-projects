from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = 'CASCADE')
    title = models.CharField(max_length=54)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) # change it to timezone.now() if problem arises
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approve_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete = 'CASCADE')
    author = models.CharField(max_length=54)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) # change it to timezone.now() if problem arises
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
