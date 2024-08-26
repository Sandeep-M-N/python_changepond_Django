from django import forms
from .models import Portfolio,feedback
 
class ProjectFieldform(forms.ModelForm):
    class Meta:
        model= Portfolio
        fields="__all__"
        labels={
            'title':"Enter the project title",
            'image':"Upload the image",
            'description':"Enter the Description of the project",
            'date':"Enter the date of the project",
            'time':"Enter the time posted ",
            'posted_by':"Enter the date posted"
        }
        error_messages={
            'title':{
                'required':"This is a required field",
                'max_length':"Maximum length can be 30",
            },
            'image':{
                'required':"This is a required field",
                'invalid_image':"please upload a valid image",
            },
            'description':{
                'required':"This is a required field",
                'max_length':"Maximum length can be 100",
            },
            'date':{
                'invalid': "Please enter a valid date in the format YYYY-MM-DD.",
                'required': "The date field is required.",
            },
            'time':{
                'invalid': "Please enter a valid time in the format HH:MM.",
                'required': "The time field cannot be empty.",
            },
            'posted_by':{
                'invalid': "Please enter a valid date in the format YYYY-MM-DD.",
                'required': "The date field is required.",
            }
        }

class Feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields="__all__"
        labels={
            'full_name':"Enter Your Name",
            'email':"Enter your email id",
            'description':"Enter your feedback",
        }
        error_messages={
            'full_name':{
                'required':"This is a required field",
                'max_length':"Maximum length can be 30",
            },
            'email':{
                'invalid': "Please enter a valid email address.",
                'required': "This is a required field",
            },
            'description':{
                'required':"This is a required field",
                'max_length':"Maximum length can be 100",
            }
        }
