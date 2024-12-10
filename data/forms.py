# forms.py
from django import forms
from .models import Post
from .models import ProfileData
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name','image', 'caption']
 
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    
        
        
class SignupForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
     
        
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
class ProfileUpdateForm(forms.Form):
    class Meta:
        model = ProfileData
        fields = ['name', 'surname', 'email', 'image', 'bio']