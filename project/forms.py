from django import forms

from .models import Project

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
    
        labels = {
            'name':'Name',
            'description':'Description',

        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the project'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Detailed description of the project'}),

        }
