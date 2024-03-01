from django import forms

from .models import Reviews, Rating_Star, Rating

class ReviewForm(forms.ModelForm): #Форма відгуків

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")

class RatingForm(forms.ModelForm):# Форма рейтингу фільму
    star = forms.ModelChoiceField(
        queryset=Rating_Star.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)