from django.shortcuts import render
from datetime import datetime

def index(request):
    info = {'f_name': 'Bekzod', 'l_name': 'Raximov', 'year': 2000}
    return render(request, 'news/index.html', info)

def about(request):
    now = datetime.now()
    return render(request, 'news/about.html', {'time': now})