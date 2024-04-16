from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from foodmileblog.models import UserProfile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class UpdateProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
    
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'

class CreateProfilePageForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'personal_website_url', 'instagram_url', 'twitter_url']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_picture': forms.ImageField(),
            'personal_website_url': forms.TextInput(attrs={'class': 'form-control'}), 
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}), 
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}), 
        }

class EditProfilePageForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'personal_website_url', 'instagram_url', 'twitter_url']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_picture': forms.ImageField(),
            'personal_website_url': forms.TextInput(attrs={'class': 'form-control'}), 
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}), 
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}), 
        }
