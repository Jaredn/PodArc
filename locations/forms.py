# forms.py
from django.forms import ModelForm
from django import forms
from locations.models import Datacenters, Cages, CageRows, Racks


class FormNewDatacenter(ModelForm):
    class Meta:
        model = Datacenters
        exclude = ['active',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': u'datacenter name', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': u'description', 'class': 'form-control'})
        }

class FormNewCage(ModelForm):
    class Meta:
        model = Cages
        exclude = ['active',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': u'datacenter name', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': u'description', 'class': 'form-control'})
        }

class FormNewCageRow(ModelForm):
    class Meta:
        model = CageRows
        exclude = ['active',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': u'datacenter name', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': u'description', 'class': 'form-control'})
        }

class FormNewRack(ModelForm):
    class Meta:
        model = Racks
        exclude = ['active',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': u'datacenter name', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': u'description', 'class': 'form-control'})
        }