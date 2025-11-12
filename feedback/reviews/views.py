from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView

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


class ThankYouView(TemplateView):

	# Class-Based View to render a "Thank You" page
	template_name = "reviews/thank_you.html" # Specifies the template to be rendered

	def get_context_data(self, **kwargs):

		# Adds custom data to the template context
		context = super().get_context_data(**kwargs) # Retrieve the default context
		context["message"] = "This Works" # Inject a custom message for the template
		return context
	

class ReviewsListView(ListView):
	"""
    Displays a list of all submitted reviews using 
	a Django LisView.
	"""
	template_name = "reviews/review_list.html"
	model = Review # The model to fetch objects from
	context_object_name = "reviews" # Name to use for the list in the template
    

class SingleReviewView(DetailView):
	"""
	Displays the details of a single review using a Django DetailView.
	Fetches the Review object based on the 'pk' provided in the URL
	"""
	template_name = "reviews/single_review.html"
	model = Review # The model to fetch a single object from


