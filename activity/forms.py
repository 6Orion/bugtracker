from django import forms

from .models import Activity

class ActivityModelForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['summary', 'content', ]

        labels = {
            'summary':'Summary',
            'content':'Description',

        }

        widgets = {
            'summary': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summary of the performed actions'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Detailed description of performed actions'}),

        }