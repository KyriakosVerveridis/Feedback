from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review


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
	

class ReviewsListView(TemplateView):
    """
    Displays a list of all submitted reviews using 
    a Django TemplateView.
    """
    template_name = "reviews/review_list.html"
    
    def get_context_data(self, **kwargs):
        """
        Extends the default context data with all Review instances.
        """
        # Get the base context from the parent TemplateView
        context = super().get_context_data(**kwargs)

        # Fetch all reviews from the database
        reviews = Review.objects.all()

        # Add the reviews to the template context
        context["reviews"] = reviews
        return context
    

class SingleReviewView(TemplateView):
    """
    Displays the details of a single review using a Django TemplateView.
    Retrieves the review based on its ID and passes it to the template.
    """
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        """
        Extends the default context data with 
        the selected Review instance.
        """
        # Get the base context from the parent TemplateView
        context = super().get_context_data(**kwargs)

        # Retrieve the review ID from the URL parameters
        review_id = kwargs["id"]

        # Fetch the corresponding Review object from the database
        selected_review = Review.objects.get(pk=review_id)

        # Add the selected review to the context for template access
        context["review"] = selected_review
        return context

