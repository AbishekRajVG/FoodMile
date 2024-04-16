from django.urls import path
from .views import (UserSignUpView, ProfileUpdateView,
                    ShowProfilePageView, EditProfilePageView, CreateProfilePageView)
from django.contrib.auth import views as auth_views

# since we're using class based view, we explicitly mention it as_views
# pk is primary key or django auto assigned of id for each blog entry

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name="signup"),
    path('update_profile/', ProfileUpdateView.as_view(), name="update-profile"),
    path('<int:pk>/password/', auth_views.PasswordChangeDoneView.as_view()),
    path('<int:pk>/profile/view', ShowProfilePageView.as_view(), name="show-profile-page"),
    path('<int:pk>/profile/edit', EditProfilePageView.as_view(), name="edit-profile-page"),
    path('profile/create', CreateProfilePageView.as_view(), name="create-profile-page"),
]