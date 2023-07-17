from django import forms

class TelegramForm(forms.Form):
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
