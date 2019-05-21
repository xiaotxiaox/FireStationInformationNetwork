from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view()),
    path('detail/', InformationDetailView.as_view()),
    path('publish/', PublishInformationView.as_view()),
]
