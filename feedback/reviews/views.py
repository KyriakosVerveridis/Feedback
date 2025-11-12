from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView


# Create your views here.


class ReviewView(FormView):
	"""
	Handles the submission of a Review using a Django FormView.
	"""
	form_class = ReviewForm # The form class to use for creating a review
	template_name = "reviews/review.html"
	success_url = "thank-you" # URL to redirect to after successful form submission

	def form_valid(self, form):
		"""
		Called when the submitted form is valid.
		"""
		form.save()
		return super().form_valid(form)
	


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


