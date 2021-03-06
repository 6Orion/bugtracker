from django import forms

from .models import Project

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'team_members']
    
        labels = {
            'name':'Name',
            'description':'Description',
            'team_members':'Team members',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the project'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Detailed description of the project'}),
            'team_members': forms.CheckboxSelectMultiple(attrs={'class':'form-check-input position-static', 'placeholder':'Select multiple team members'}),
        }
