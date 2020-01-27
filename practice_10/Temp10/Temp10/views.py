# Ive created this file-Shawon

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    admit = {'name': 'Shawon', 'place': 'Earth'}
    return render(request, 'hot_files.html', admit)


def home1(request):
    return HttpResponse("<h1>This is homepage1<h1/>")


def home2(request):
    djtext = request.GET.get('grabbed', 'off')
    print(djtext)
    removepunc = request.GET.get('removepunc', 'default')
    print(removepunc)
    analyzed = ""

    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'removes punctuations', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'text.html', params)
    else:
        return HttpResponse("Error!!")


def home3(request):
    return HttpResponse("<h1>This is homepage3<h1/>")
