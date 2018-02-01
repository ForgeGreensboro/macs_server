from django.urls import path

from . import views

urlpatterns = [
    path('',views.MachineView.as_view(), name='index')
]