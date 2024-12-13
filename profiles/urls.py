
from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('profiles/', views.ProfileView.as_view(), name="profiles"),
    path('profile/', views.AdminProfile.as_view(), name="profile"),
    path('profile/update/', views.ProfileUpdateView.as_view(), name="update-profile"),
    path('detail//user/<int:pk>', views.ProfileDetail.as_view(), name='detail'),


]