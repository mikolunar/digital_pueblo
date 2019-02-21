from django.forms import ModelForm
from django import forms
from . models import Anuncio

class AddAnuncioForm(ModelForm):

    class Meta:
        model= Anuncio
        fields = "__all__"


class EditAnuncioForm(ModelForm):

    class Meta:
        model=Anuncio
        fields ="__all__"


class ContactForm(ModelForm):
    subject=forms.CharField(max_length=100)
    message=forms.CharField()
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)

