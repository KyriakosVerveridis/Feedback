from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm


# Create your views here.

def review(request):
	"""
	Handles the review form:
    - Displays an empty form on GET requests.
    - Processes submitted form data on POST.
    - Redirects to the thank-you page after successful validation.
	"""
	if request.method == "POST":
		form = ReviewForm(request.POST)

		# Validate the form before accessing cleaned_data
		if form.is_valid():
			print(form.cleaned_data)  # Debug: display validated form data
			return HttpResponseRedirect("thank-you") 	
	
	else:
		# Show an empty or unvalidated form
		form = ReviewForm()
	
	context = {"form":form
						}
	# Render the form page with its context
	return render(request, "reviews/review.html", context)


def thank_you(request):
	"""
	Renders the thank-you page after a successful form submission.
	"""
	return render (request,"reviews/thank_you.html")