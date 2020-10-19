import requests
from django.shortcuts import render, redirect,get_object_or_404
from .models import Note
from weather.forms import NoteForm


def note_index(request):
    former = Note.objects.all()

    form = NoteForm(request.POST)
    if form.is_valid():
        form.save()
        form = NoteForm()

    context = {
        'post': former,
        'form': form
    }

    return render(request,'note/note.html',context)

def create_note(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        form.save()
        form = NoteForm()
    
    context = {
        'form':form
    }
    return render(request,'note/note_create.html',context)

def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('../../')