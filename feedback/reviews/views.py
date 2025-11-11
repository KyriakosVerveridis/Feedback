from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review


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

			# Create a new Review instance using the validated form data
			review = Review(
				user_name=form.cleaned_data["user_name"], # get user_name from form
				review_text=form.cleaned_data["review_text"], # get review_text from form
				rating=form.cleaned_data["rating"]) # get rating from form
			review.save() # Save the data
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