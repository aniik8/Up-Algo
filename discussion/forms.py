from django import forms
from .models import Discussion

class Form(forms.ModelForm):
    
    class Meta:
        model = Discussion
        fields = '__all__'


