from django.urls import path, include
from polls.views import HomeView, QuestionView


urlpatterns = [
    path(r'home', HomeView.as_view(), name='home'),
    path(r'question', QuestionView.as_view(), name='question'),
]