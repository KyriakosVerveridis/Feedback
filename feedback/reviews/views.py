from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View


# Create your views here.


class ReviewView(View):
	"""
	Using a class-based view allows a cleaner separation of HTTP methods
    and makes the view more organized and reusable.
	"""
	def get(self, request):

		# Handle GET requests: display an empty review form
		form = ReviewForm()
		context = {"form":form}
		return render(request, "reviews/review.html", context)

	def post(self, request):

		# Handle POST requests: process submitted form data
		form = ReviewForm(request.POST)

		# Validate the form before saving
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("thank-you") 
	
		context = {"form":form}
		return render(request, "reviews/review.html", context)	


def thank_you(request):
	"""
	Renders the thank-you page after a successful form submission.
	"""
	return render (request,"reviews/thank_you.html")