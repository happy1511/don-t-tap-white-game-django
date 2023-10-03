from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Score
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
import json
from datetime import date
# Create your views here.


def home(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'Main.html')
    else:
        try:
            user = User.objects.create_user(
                request.POST['username'],
                password=request.POST['password']
            )
            user.save()
            login(request, user)
            userObject = Score(
                username=request.POST['username'], highestscore='0', history=list([]))
            userObject.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'SignUp.html', {'error': 'Username already taken. Choose new username.'})


def game(request):
    AllScores = Score.objects.all()
    return render(request, 'Game.html', {'Tiles': AllScores})


def signup(request):
    return render(request, 'SignUp.html')


def logoutaccount(request):
    if User.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        redirect('signup')


def loginaccount(request):

    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'error': 'user not found'})
        else:
            login(request, user)
            return redirect('home')


def SerachUserData(username, Arr):
    for i in Arr:
        print(username, i)
        # print(i.username,username)
        if i.username == username:
            return i
    return None


def addscore(request):
    if (User.is_authenticated):
        score = (json.loads(request.body.decode('utf-8')))['Score']
        username = (json.loads(request.body.decode('utf-8')))['username']
        AllScores = Score.objects.all()
        Object = AllScores
        Searched = SerachUserData(username, Object)
        print(Searched, 'sera')
        if Searched != None:
            if (int(Searched.highestscore) < score):
                Searched.highestscore = score
                print(Searched.highestscore)
            Searched.history.append({(date.today()): score})
            Searched.save()
            print(Searched.highestscore)
            print(Searched.history)
            print(Searched.username)
            return render(request, 'Main.html')
        else:
            return HttpResponse('No database Found')
    else:
        return HttpResponse('Not Logged in')


def datesFromResponse(Arr):
    new = []
    for i in Arr:
        new.append(list(i.keys()))
    return new


def scoresFromResponse(Arr):
    new = []
    for j in Arr:
        new.append(list(j.values()))
    return new


def PreviousScore(request):
    if (User.is_authenticated):
        scores = SerachUserData(request.user.username, Score.objects.all())
        dates = datesFromResponse(scores.history)
        dateScores = scoresFromResponse(scores.history)
        print(list(scores.history))
        print(scoresFromResponse(list(scores.history)))
        print(datesFromResponse(list(scores.history)))
        return render(request, 'historicalData.html', {'dates': dates, 'scores': dateScores,'highest':scores.highestscore})
    else:
        return render(request, 'SignUp.html')
