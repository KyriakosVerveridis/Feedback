from django import forms
from .models import Review

# # ReviewForm: A simple Django form for collecting user reviews
# class ReviewForm(forms.Form):
# 	user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
# 		"required": "Your name must not be empty!",
# 		"max_length": "Please enter a shorter name!"
# 	})
# 	review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
# 	rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

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
        
        
