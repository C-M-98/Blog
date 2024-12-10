from django.contrib import admin
from .models import Post
from .forms import PostForm, SignupForm
from .models import ProfileData
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    form=PostForm
    name = 'data'
class ProfileDataAdmin(admin.ModelAdmin):
    form = SignupForm
    name='data'
admin.site.register(Post, PostAdmin)
admin.site.register(ProfileData, ProfileDataAdmin)