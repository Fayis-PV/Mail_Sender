from .models import Recipients
from django import forms

class RecipientsForm(forms.ModelForm):
    class Meta:
        model = Recipients
        fields = ('name','email','file')