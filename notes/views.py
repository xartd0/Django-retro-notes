from django.shortcuts import render
from .models import Note
from django.shortcuts import redirect
from django.http import HttpResponse
import uuid


def index(request):
    return render(request, 'index.html')

def add_note(request):
    if request.method == 'POST':
        new = Note.objects.create(text=request.POST['text'], uniq=uuid.uuid4())
        new.save
        return redirect(f'/note/{new.uniq}')


def note(request, uniqid):
    note = Note.objects.filter(uniq=uniqid).first()
    if note != None:
        context = {'secret_message': note.text,
                'secret_title': note.id }
        return render(request, 'note.html', context)
    else:
        return HttpResponse("404")