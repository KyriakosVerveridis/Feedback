from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def review(request):
	"""
	Handles user review form submissions.
    - Displays the review form on GET requests.
    - Processes submitted data and redirects to a thank-you page on POST.
	"""
	if request.method == "POST":
		entered_username = request.POST["username"]
		print(entered_username) 
		return HttpResponseRedirect("thank-you")
	
	return render(request, "reviews/review.html")


def thank_you(request):
	"""
	Renders the thank-you page after a successful form submission.
	"""
	return render (request,"reviews/thank_you.html")