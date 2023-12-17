from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def method_used(request):

    if request.method == 'POST':
        return HttpResponse('Thanks for submitting the Health form.')
    else:
        return HttpResponse(request.method)