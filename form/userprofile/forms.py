from django import forms
from .models import Review

# class feedbackform(forms.Form):
#     user_name=forms.CharField(label='Enter the name',max_length=20,
#                               error_messages={
#                                   'required':"it is a empty value",
#                                   'max_length':"please enter a shorter name"
#                               })
#     rating=forms.IntegerField(label="enter your rating",min_value=5,max_value=10,
#                               error_messages={
#                                   'required':"it cannot be empty",
#                                   'min_value':"it cannot be less than 5",
#                                   'max_value':"it cannot be more than 10"
#                               })
#     message=forms.CharField(label="Enter the message here",widget=forms.Textarea,max_length=100,
#                             error_messages={
#                                 'required':"it cannot be empty",
#                                 'max_length':"it should not be exceed 100 words"
#                             })

class feedbackform(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' #['user_name',rating]
        #exclude = []
        labels = {
            'user_name':'Your Name',
            'text':'enter the feedback',
            'rating':'Enter the rating'
        }
 

    