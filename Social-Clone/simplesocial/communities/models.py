from django.db import models
from django.utils.text import slugify

import misaka
from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library()
from django.urls import reverse

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html =models.TextField(editable=False, blank=True, default='')
    members = models.ManyToManyField(User,through='CommunityMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('communities:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class CommunityMember(models.Model):
    community = models.ForeignKey(Community, related_name = 'memberships',on_delete = 'NULL')
    user = models.ForeignKey(User, related_name='user_communities', on_delete ='NULL')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('community','user')
