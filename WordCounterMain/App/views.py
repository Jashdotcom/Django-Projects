from pydoc import text
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def counter(request):
    text = request.POST.get('text', '')
    word_count = len(text.split())
    return render(request, 'counter.html', {'word_count': word_count})