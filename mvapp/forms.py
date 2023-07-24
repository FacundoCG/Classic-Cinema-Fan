from django import forms
from django.core.exceptions import ValidationError
from .models import Movie
from ckeditor.widgets import CKEditorWidget

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'description', 'rating', 'genders', 'company', 'premiere', 'image']
        RATING = [
            (1, "Very bad"),
            (2, "Bad"),
            (3, "Mediocre"),
            (4, "Good"),
            (5, "Excellent"),
        ]   
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Movie'}),
            'description': CKEditorWidget(),
            'rating':forms.Select(attrs={'class':'form-control', 'placeholder':'Rating'}),
            'genders':forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Genres'}),
            'company':forms.Select(attrs={'class':'form-control', 'placeholder':'Company'}),
            'premiere':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Release date'}),
            'image':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Cover'}),
        }
        
        labels = {
            'name': 'Movie name',
            'description':'Description',
            'genders':'Genres',
            'company':'Company',
            'premiere':'Premiere',
            'image':'Image',
        }
    
    def clean_premiere(self):
        data = self.cleaned_data['premiere']

        if data < 1930:
            raise ValidationError(('There are not movies before 1930'))

        return data