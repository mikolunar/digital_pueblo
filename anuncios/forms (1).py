from django.forms import ModelForm
from django import forms
from . models import Anuncio


class AddAnuncioForm(ModelForm):

    class Meta:
        model = Anuncio
        fields = "__all__"

    def clean(self):
        super(AddAnuncioForm, self).clean()
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._errors['title'] = self.error_class(
                ['Minimum 5 characters required'])

        return self.cleaned_data


class EditAnuncioForm(ModelForm):

    class Meta:
        model = Anuncio
        fields = "__all__"

    def clean(self):
        super(EditAnuncioForm, self).clean()
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._errors['title'] = self.error_class(
                ['Minimum 5 characters required'])

        return self.cleaned_data


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
