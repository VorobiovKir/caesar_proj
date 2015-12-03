from django import forms

from .models import Transcription


class TranscriptionForm(forms.ModelForm):
    legend = forms.CharField(
        max_length=32,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-5 col-sm-5 col-lg-5 col-xs-5',
                'placeholder': 'Pls fill briefly description',
                'aria-describedby': 'sizing-addon1',
                'ng-model': 'legend'
            }
        )
    )

    text_origin = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control cont_usr_text col-md-5',
                'placeholder': 'Enter your normal text',
                'ng-model': 'user_text'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(TranscriptionForm, self).__init__(*args, **kwargs)
        self.fields['rot'].widget.attrs = {
            'class': 'rot',
            'ng-model': 'rot',
            'min': 0,
        }

    class Meta:
        model = Transcription
        fields = ['legend', 'text_origin', 'rot', 'encrypt']
