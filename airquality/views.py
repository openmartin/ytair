# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from check_in.models import Person, Check
from datetime import datetime, date
from django.core.context_processors import csrf
from check_in.utils import test_has_ball

def home(request):
    has_ball = test_has_ball(date.today())
    print has_ball
    persons = Person.objects.filter(isvalid='Y')
    play_date = date.today()
    has_family = 'N'
    family_member_amount = 0
    c = {'persons':persons,
         'has_ball':has_ball,
         'play_date':play_date}
    c.update(csrf(request))
    return render_to_response('poll.html',c)
    
def query(request):
    has_ball = test_has_ball(date.today())
    play_date = date.today()
    check_qs = Check.objects.filter(play_date=play_date)
    print check_qs
    c = {'checks':check_qs,
         'has_ball':has_ball,
         'play_date':play_date}
    return render_to_response('query.html', c)

def check(request):
    play_date_str = request.POST.get("play_date", date.today().strftime('%Y-%m-%d'))
    play_date = datetime.strptime(play_date_str, '%Y-%m-%d').date()
    person_id = int(request.POST.get("person", -1))
    has_family = request.POST.get("has_family", "N")
    family_member_amount = int(request.POST.get("family_member_amount", 0))
    check_time = datetime.now()
    
    if person_id == -1:
        return redirect("query")
    
    if family_member_amount == 0:
        has_family = "N"
    
    print play_date
    print person_id
    print has_family
    print family_member_amount
    print check_time
    
    person = Person.objects.get(pk=person_id)
    
    check_qs = Check.objects.filter(play_date=play_date, person_id=person_id)
    print check_qs
    if len(check_qs) == 0:
        check = Check()
    else:
        check = check_qs[0]
    
    #save
    check.play_date = play_date
    check.person = person
    check.has_family = has_family
    check.family_member_amount = family_member_amount
    check.check_time = check_time
    check.save()
    return redirect("query")

def cancel(request):
    play_date_str = request.POST.get("play_date", date.today().strftime('%Y-%m-%d'))
    play_date = datetime.strptime(play_date_str, '%Y-%m-%d').date()
    person_id = int(request.POST.get("person", -1))
    has_family = request.POST.get("has_family", "N")
    family_member_amount = int(request.POST.get("family_member_amount", 0))
    check_time = datetime.now()
    
    if person_id == -1:
        return redirect("query")
    
    if family_member_amount == 0:
        has_family = "N"
    
    print play_date
    print person_id
    print has_family
    print family_member_amount
    print check_time

    person = Person.objects.get(pk=person_id)
    
    check_qs = Check.objects.filter(play_date=play_date, person_id=person_id)
    print check_qs
    if not len(check_qs) == 0:
        check = check_qs[0]
        check.delete()
        
    return redirect("query")
