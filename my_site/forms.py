from django import forms

class TelegramForm(forms.Form):
    TelegremMessage = forms.CharField(label="Обратная связь:", widget=forms.Textarea)
