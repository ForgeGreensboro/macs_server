from django.urls import re_path, include

from .views import HomeView

urlpatterns = [
	re_path('', HomeView.as_view())
]