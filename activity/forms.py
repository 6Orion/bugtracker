from django import forms

from .models import Activity

class ActivityModelForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['summary', 'bug', 'content', ]

        labels = {
            'summary':'Summary',
            'content':'Description',
            'bug':'Parent bug'
        }

        widgets = {
            'summary': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summary of the performed actions'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Detailed description of performed actions'}),
            'bug':     forms.Select(attrs={'class':'form-control', 'placeholder':'Please select a bug'}),
        }