


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'data'

urlpatterns = [
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('signup/' ,views.SignUp.as_view(), name='signup'),
    

]