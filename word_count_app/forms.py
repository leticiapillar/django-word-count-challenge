from django import forms
from .models import WordCountModel

class WordCountForm(forms.ModelForm):
    text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                # "placeholder": "Typing any text...",
                "class": "form-control",
            }
        ),
        label="Type a text",
    )

    class Meta:
        model = WordCountModel
        # exclude = ("total_words",)
        fields = ["text"]

