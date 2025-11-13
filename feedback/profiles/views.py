from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


class CreateProfileView(View):
    # Handles displaying and submitting the profile creation form

    def get(self, request):
        # Render empty profile form
        form = ProfileForm()
        context = {"form": form}
        return render(request, "profiles/create_profile.html", context)

    def post(self, request):
        # Handle form submission with POST data and uploaded files
        submited_form = ProfileForm(request.POST,request.FILES)

        if submited_form.is_valid():
            # Create a new UserProfile with the uploaded image and save it
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")

        # Re-render form with validation errors
        context = {"form":submited_form}
        return render(request, "profiles/create_profile.html", context)
