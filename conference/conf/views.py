from django.shortcuts import render
from conf.models import Room, Reservation
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from datetime import datetime
from django.db import IntegrityError


def add_room(request):
    if request.method == "GET":
        return render(request, "add_room.html")
    else:
        name = request.POST.get('name')
        seats = request.POST.get('seats')

        r = Room()
        r.name = name
        r.seats = seats
        if request.POST.get('projector'):
            r.projector = True
        else:
            r.projector = False
        r.save()
        return redirect('/rooms')

def rooms(request):
    d = datetime.today().strftime('%d-%m-%Y')
    r = Room.objects.all()

    return render(request, "rooms.html", {'room':r, 'date':d})

def room_details(request, id):
    r = Room.objects.get(pk=id)
    res = Reservation.objects.filter(room_id=id, date__gte=datetime.today())
    return render(request, "room_details.html", {'room':r, 'res':res})

def edit_room(request,id):
    r = Room.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "edit_room.html",  {'room':r})
    else:
        name = request.POST.get('name')
        seats = request.POST.get('seats')

        r.name = name
        r.seats = seats
        if request.POST.get('projector'):
            r.projector = True
        else:
            r.projector = False
        r.save()
        return redirect('/rooms')

def delete_room(request, id):
    r = Room.objects.get(pk=id)
    r.delete()
    return HttpResponse("Usunięto salę!<br><a href='/rooms'>Powrót</a>")

def reservation(request, id):
    if request.method == "GET":
        r = Room.objects.get(pk=id)
        res = Reservation.objects.filter(room_id=id, date__gte=datetime.today())
        return render(request, "reservation.html", {'room': r, 'res':res})
    else:
        date = request.POST.get('date')
        comment = request.POST.get('comment')

        if date < datetime.today().strftime('%Y-%m-%d'):
            return HttpResponse("Data rezerwacji nie może być z przeszłości!<br><a href='/rooms'>Powrót</a>")

        try:
            res = Reservation()
            res.date = date
            res.comment = comment
            res.room_id = id
            res.save()
            return redirect('/rooms')
        except IntegrityError:
            return HttpResponse("Sala jest już zarezerwowana w wybranym terminie!<br><a href='/rooms'>Powrót</a>")


def search(request):
    if request.method == "GET":
        return render(request, "search.html")
    else:
        seats = request.POST.get('seats')
        date = request.POST.get('date')
        projector = request.POST.get('projector')

        if seats and date and projector:
            room = Room.objects.filter(seats__gte=seats, projector=True).exclude(reservation__date=date)
        elif seats and date:
            room = Room.objects.filter(seats__gte=seats, projector=False).exclude(reservation__date=date)

        if room:
            return render(request, "found.html", {'room': room, 'date': date})
        else:
            return HttpResponse("Brak wolnych sal dla podanych kryteriów wyszukiwania <br><a href='/search'>Powrót</a>")
