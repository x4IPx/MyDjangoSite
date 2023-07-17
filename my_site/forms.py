from django import forms

class TelegramForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
