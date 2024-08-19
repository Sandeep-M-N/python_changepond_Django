from django import forms

class feedbackform(forms.Form):
    user_name=forms.CharField(label='Enter the name')