from django.views.generic  import ListView
from django.shortcuts import render

from macs.models.log import MachineLock, MachineUnlock

class HomeView(ListView):
	template_name = "home/index.html"

	def get(self, request, *args, **kwargs):
		return super().get(request, args, kwargs)

	def get_queryset(self):
		return MachineLock.objects.all()