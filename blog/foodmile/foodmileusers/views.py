from django.shortcuts import get_object_or_404, render
from django.views import generic
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import (RegisterForm, UpdateProfileForm, 
                    CreateProfilePageForm, EditProfilePageForm)
from django.urls import reverse, reverse_lazy
from foodmileblog.models import UserProfile

class UserSignUpView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_url = reverse_lazy('create-profile-page')
    

class ProfileUpdateView(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class ShowProfilePageView(generic.DeleteView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = UserProfile.objects.all() instead of getting all get from pk
        page_user = get_object_or_404(UserProfile, id=str(self.kwargs['pk']))
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        context["page_user"] = page_user

        return context
    
class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_user_profile.html'
    # fields = ['bio', 'profile_picture', 'personal_website_url', 'instagram_url', 'twitter_url']
    success_url = reverse_lazy('home')


class CreateProfilePageView(generic.CreateView):
    model = UserProfile
    form_class = CreateProfilePageForm
    template_name = 'registration/create_user_profile.html'

    def form_valid(self, form):
        print("self.request.user: " + str(self.request.user) )
        form.instance.user_profile = self.request.user 
        return super().form_valid(form)