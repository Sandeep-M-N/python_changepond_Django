from django.shortcuts import render
from django.views.generic.edit import CreateView
from.models import Post,Comment,Tags,Author

# Create your views here.
class CommentView(CreateView):
    model=Comment
    template_name='task1/comment.html'
    success_url='thankyou'