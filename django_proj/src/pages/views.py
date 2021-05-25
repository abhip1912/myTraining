from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request):
    my_context = {
        'my_text': 'This is about us',
        'my_num': 123,
        'my_list': ['abhi', 'shek', 123, 'patil']
    }
    return render(request, 'home.html', my_context)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
