from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .forms import PostForm, LoginForm
from .forms import SignupForm, LoginForm
from data.models import ProfileData
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
class CreatePost(CreateView):
    form_class = PostForm
    template_name = 'data/create_post.html'
    success_url = reverse_lazy('home')
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    
class HomeFeed(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'data/feed.html'
    context_object_name = 'posts'
    success_url = 'home/'


class SignUp(FormView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('data:login')
    
    def create_profile(user,form):
        user = form.save()
        ProfileData.objects.create(user=user)
    def save_profile(user, form):
        user = form.save()
        if hasattr(user, 'profile'):
            user.profile.save()

        
class LoginView(FormView):
    template_name = 'registration/login.html'
    success_url = '/home/'
    form_class = LoginForm 
    
    def form_valid(self, form):
        # Get the cleaned data
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # Authenticate the user
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user) 
        return redirect(self.success_url)  # Log the user  # Redirect to success_url


    
class CreatePost(FormView):
    form_class = PostForm
    template_name = 'data/create_post.html'
    success_url = '/home/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
        
