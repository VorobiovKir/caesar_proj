from django.shortcuts import render

from .forms import TranscriptionForm


def main(request):

    return render(request, 'main.html', {'form': TranscriptionForm})
