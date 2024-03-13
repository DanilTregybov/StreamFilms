from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Reviews, Rating_Star, Rating

class ReviewForm(forms.ModelForm): #Форма відгуків

    captcha = ReCaptchaField()
    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }

class RatingForm(forms.ModelForm):# Форма рейтингу фільму
    star = forms.ModelChoiceField(
        queryset=Rating_Star.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)