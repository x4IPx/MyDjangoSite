from django import forms

class TelegramForm(forms.Form):
    TelegremMessage = forms.CharField( label="" ,  help_text="Пожалуйста, расскажите, что именно вам не понравилось/смутило в моем резюме, а также поделитесь своими пожеланиями и рекомендациями. Я буду благодарен за ваш отзыв.", widget=forms.Textarea)
