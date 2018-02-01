from django import forms


class MachineForm(forms.Form):
    description = forms.CharField()
    address = forms.CharField()