from django import forms

from .models import Transcription


class TranscriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TranscriptionForm, self).__init__(*args, **kwargs)
        self.fields['legend'].label = 'title'

    class Meta:
        model = Transcription
        fields = ['legend', 'text_origin', 'rot']
