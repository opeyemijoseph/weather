import requests
from django.shortcuts import render, redirect
from .models import Note
from weather.forms import NoteForm


def index(request):
    former = Note.objects.all()

    form = NoteForm(request.POST)
    if form.is_valid():
        form.save()
        form = NoteForm()
        
    context = {
        'post': former
    }
    return render(request, 'note/note.html', context)

    form = NoteForm(request.POST)
    if form.is_valid():
        form.save()
        form = NoteForm()
    
    context = {
        'form':form
    }
    return render(request,'note.html',context)

def create_note(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        form.save()
        form = NoteForm()
    
    context = {
        'form':form
    }
    return render(request,'note/note_create.html',context)

#def delete_note(request, city_name):
    #Note.objects.get(name=city_name).delete()
    #return redirect('../../')