from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class HomeView(View):
    """Knowledge home View."""

    def get(self, request, *args, **kwargs):
        return render(request, "home.html")