from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka
from communities.models import Community

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'posts', on_delete ='NULL')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    community = models.ForeignKey(Community, related_name='posts', null=True,blank=True,on_delete= 'NULL')

    def __str__(self):
        return self.message

    def save(self, *args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
