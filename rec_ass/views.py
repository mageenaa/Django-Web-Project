from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul' : 'Tugas Besar',
        'lab' : 'MBC Laboratory',
    }
    return render(request, 'index.html', context)

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    return render(request, 'register.html')

def counter(request):
    text = request.POST['text']
    total_kata = len(text.split())
    return render(request, 'counter.html', {'total_kata' : total_kata})