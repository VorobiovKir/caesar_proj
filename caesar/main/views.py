from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseBadRequest

from .forms import TranscriptionForm
from .methods import encrypting


def main(request):
    if request.is_ajax():
        response = {}
        legend = request.GET.get('legend')
        text = request.GET.get('text')
        rot = request.GET.get('rot')
        reverse = request.GET.get('reverse') or False

        post_form = TranscriptionForm(
            {
                'legend': legend,
                'rot': rot,
                'text_origin': text,
                'encrypt': reverse
            }
        )

        if post_form.is_valid():
            post_form.save()
        else:
            error = post_form.errors
            return HttpResponseBadRequest(JsonResponse(error))

        response['result'] = encrypting(text, rot, reverse)

        return HttpResponse(JsonResponse(response))
    else:
        args = {}
        args['form'] = TranscriptionForm

    return render(request, 'main.html', args)
