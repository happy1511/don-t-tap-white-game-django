from django.shortcuts import render
from .models import Tile

# Create your views here.

def home(request):
    return render(request,'Main.html')

def game(request):
    AllTiles = Tile.objects.all()
    return render(request,'Game.html',{'Tiles':AllTiles})