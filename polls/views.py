from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages

# Create your views here.


class HomeView(View):
    """Knowledge home View."""

    def get(self, request, *args, **kwargs):
        return render(request, "home.html")
    

class QuestionView(View):
    """Knowledge home View."""

    def get(self, request, *args, **kwargs):
        # messages.success(request, "Your request for a Knowledge Service Provider has been logged Successfully")
        return render(request, "add_questions.html")
    
    def post(self, request, *args, **kwargs):
        # Post method
        messages.success(request, "Your Question has been added Successfully")
        return render(request, "add_questions.html")
