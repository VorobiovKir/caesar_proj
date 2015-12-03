from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from .forms import TranscriptionForm
from .methods import encrypting


def main(request):
    args = {}
    args['result'] = ''
    # response = JsonResponse(args)
    # print response.content
    if request.is_ajax():
        arg = {}
        arg['test'] = 'snsfdsad'
        arg['count'] = 3
        response = JsonResponse(arg)
        return HttpResponse(response)
    if request.POST:
        text = request.POST.get('text_origin')
        rot = request.POST.get('rot')
        args['result'] = encrypting(text, rot)

    args['form'] = TranscriptionForm

    return render(request, 'main.html', args)


def ajax_test(request):
    response = {}
    if request.is_ajax:
        text = request.GET.get('text')
        rot = request.GET.get('rot')
        response['result'] = encrypting(text, rot)

        # if request.method == 'POST':
        #     message = 'is_ajax_post'
        #     print '--------------'
        #     print request.GET.get('text')
        #     print '--------------'
        #     print request.GET.get('rot')
        # arg = {}
        # arg['test'] = 'snsfdsad'
        # arg['count'] = 3
        # response = JsonResponse(arg)
        # return HttpResponse(response)
    else:
        response['error'] = "something goes wrong"
    return HttpResponse(JsonResponse(response))
