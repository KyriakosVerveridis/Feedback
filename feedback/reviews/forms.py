from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    A Django ModelForm that automatically generates form fields 
    based on the Review model.
    """
    class Meta:
        model = Review # Specifies the model that this form is based on
        fields = "__all__"
        # exclude = ["owner_comment"]
		# Custom labels for form fields displayed in the UI
        
        labels = {
            "user_name": "Your Name",
            "review_text":"Your Feedback",
            "rating":"Your Rating"
		}
        
        # Custom validation error messages for specific fields
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
            	"max_length": "Please enter a shorter name!"
			}
		}
        
        
