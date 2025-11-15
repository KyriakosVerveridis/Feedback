from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


# Create your views here.


class ReviewView(CreateView):
	"""
	Handles the submission of a Review using a Django FormView.
	"""
	model = Review # The model to create an instance of
	form_class = ReviewForm # The form class used for creating a review
	template_name = "reviews/review.html"
	success_url = "thank-you" # URL to redirect to after successful form submission


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

	def get_context_data(self, **kwargs):
		# Get the default context from DetailView (includes the object by default)
		context = super().get_context_data(**kwargs)
		# The object fetched by the DetailView
		loaded_review = self.object
		# Access the request object to read session data, user info, etc.
		request = self.request
		 # Retrieve the 'favorite_review' id from the user's session
		favorite_id = request.session.get("favorite_review")
		# Add a custom variable to the context for the template
    	# True if the current review is the user's favorite, else False
		context["is_favorite"] = favorite_id == str(loaded_review.id)
		return context



class AddFavoriteView(View):
	"""
	# Retrieve the Review instance that corresponds to the submitted review_id.
	"""
	def post(self,request):
		review_id = request.POST["review_id"]
		request.session["favorite_review"] = review_id
		return HttpResponseRedirect("/reviews/" + review_id)