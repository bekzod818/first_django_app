from django import forms
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# This function Add and Show Students
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            reg = User(name = nm, email = em, password = pw)
            reg.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    students = User.objects.all()
    content = {'form': form, 'stud': students}
    return render(request, 'enroll/addandshow.html', content)

# This function will Edit/Update 
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': form})

# This function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
