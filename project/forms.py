from django import forms

from .models import Project

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
    
        # example of additional editing capabilities for ModelForm class
        
        # labels  = {
        #     'title':'Titulo', 
        #     'publication_date':'Data de Publicação', 
        #     'author':'Autor', 
        #     'price':'Preço', 
        #     'pages':'Número de Páginas',
        #     'book_type':'Formato'
        #     }
        # widgets = {
        #     'title': forms.TextInput(attrs={'class':'form-control'}),
        #     'publication_date': forms.TextInput(attrs={'class':'form-control'}),
        #     'author': forms.TextInput(attrs={'class':'form-control'}),
        #     'price': forms.TextInput(attrs={'class':'form-control'}),
        #     'pages': forms.TextInput(attrs={'class':'form-control'}),
        #     'book_type': forms.TextInput(attrs={'class':'form-control'}),
        # } 