from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm

# Create your views here.


def store_file(file):

    # Open destination file in binary write mode
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


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
            # Save uploaded image to local storage
            store_file(request.FILES["image"])
            return HttpResponseRedirect("/profiles")

        # Re-render form with validation errors
        context = {"form":submited_form}
        return render(request, "profiles/create_profile.html", context)
