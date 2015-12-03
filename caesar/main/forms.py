from django import forms

from .models import Transcription


class TranscriptionForm(forms.ModelForm):
    legend = forms.CharField(
        max_length=32,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-5 col-sm-5 col-lg-5',
                'id': 'origin text',
                'placeholder': 'Pls fill briefly description',
                'aria-describedby': 'sizing-addon1'
            }
        )
    )

    text_origin = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control cont_usr_text col-md-5',
                'placeholder': 'Enter your normal text',
            }
        )
    )

    class Meta:
        model = Transcription
        fields = ['legend', 'text_origin', 'rot']
