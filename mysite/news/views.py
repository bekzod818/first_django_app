from django.shortcuts import render, redirect
from datetime import datetime
from .models import Tutorial
from .forms import TutorialForm

def index(request):
    info = {'f_name': 'Bekzod', 'l_name': 'Raximov', 'year': 2000}
    return render(request, 'news/index.html', info)

def about(request):
    now = datetime.now()
    return render(request, 'news/about.html', {'time': now})

def news(request):
    content = Tutorial.objects.all()
    return render(request, 'news/news.html', {'news': content})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Xatolik yuz berdi!'
    
    form = TutorialForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/add.html', data)