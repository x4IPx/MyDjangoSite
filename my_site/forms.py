from django import forms

class TelegramForm(forms.Form):
    TelegremMessage = forms.CharField(label="Комментарий", widget=forms.Textarea)
