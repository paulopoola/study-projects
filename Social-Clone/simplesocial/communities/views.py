from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from communities.models import Community, CommunityMember
from django.contrib import messages
from . import models 
# Create your views here.
class CreateCommunity(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Community

class SingleCommunity(generic.DetailView):
    model = Community

class ListCommunities(generic.ListView):
    model = Community

class JoinCommunity(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('communities:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        community = get_object_or_404(Community, slug=self.kwargs.get('slug'))
        try:
            CommunityMember.object.create(user=self.request.user, community=community)
        except:
            messages.warning(self.request,'You are already a member of this Community!')
        else:
            messages.success(self.request,'You are now a member of this Community')
        return super().get(request,*args,**kwargs)

class LeaveCommunity(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('communities:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = models.CommunityMember.objects.filter(
                user = self.request.user,
                community__slug = self.kwargs.get('slug')
            ).get()
        except models.CommunityMember.DoesNotExist:
            messages.warning(self.request,'You are not a member of this Community!')
        else:
            membership.delete()
            messages.success(self.request,'You have left the Community!')
        return super().get(request,*args,**kwargs)
