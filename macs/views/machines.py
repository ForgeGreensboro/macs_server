from django.shortcuts import render
from django.views import generic

class MachineView(generic.ListView):
    template_name = 'macs/index.html'

    def get_queryset(self):
        pass