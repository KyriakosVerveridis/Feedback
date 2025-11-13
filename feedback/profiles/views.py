from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.


class CreateProfileView(CreateView):
    """
    Django CreateView to handle displaying the form 
    and creating a new UserProfile
    """

    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles/"


class ProfileView(ListView):
    template_name = "profiles/user_profiles.html"
    model = UserProfile
    context_object_name = "profiles"