from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from data.models import ProfileData
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView






class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'profiles/profiles.html'
    model = ProfileData
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = ProfileData.objects.all()
        return context
    
    # def get_queryset(self):
    #     return ProfileData.objects.all()
    
class AdminProfile(TemplateView):
    template_name = 'profiles/profile.html'
    model = ProfileData
    context_object_name = 'profile_detail'
    
    def get_object(self, queryset=None):
        return ProfileData.objects.get(user=self.request.user)
class ProfileDetail(DetailView):
    model = ProfileData
    template_name = 'profiles/detailed-profile.html'
    context_object_name = 'detail-profile'
    
    def get_object(self, queryset=None):
        return ProfileData.objects.get(user__pk=self.kwargs['pk'])
    
# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = ProfileData
#     form_class = ProfileUpdateForm
#     template_name = 'profiles/profile.html'
#     context_object_name = 'profile'
    
#     def get_object(self, queryset=None):
#         return ProfileData.objects.get(user=self.request.user)
    
#     def get_success_url(self):
#         return reverse_lazy('profile')




    
