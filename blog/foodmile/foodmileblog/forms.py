from django import forms
from .models import Post, Category, User, Comment

from django.contrib.auth.forms import PasswordChangeForm

categories = list(Category.objects.all().values_list('name', 'name')) # two times because it works like that weird, cast to list

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), # here class form-control is a bootstarp class
            'category': forms.Select(choices=categories, attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'header_image': forms.ImageField(),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), # here class form-control is a bootstarp class
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateProfilePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), # here class form-control is a bootstarp class
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateProfilePassword(PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
    
    def __init__(self, *args, **kwargs):
        super(UpdateProfilePassword, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['type'] = 'password'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['type'] = 'password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['type'] = 'password'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]

        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }