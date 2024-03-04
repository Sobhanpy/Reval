from django.urls import path, include
from root.views import HomeView
urlpatterns = [
    path('', HomeView.as_view, name = "Home")
]