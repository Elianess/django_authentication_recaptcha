from django import forms
from django_recaptcha.fields import ReCaptchaField

class TaskForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    captcha = ReCaptchaField()