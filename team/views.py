# Create your views here.
from django.shortcuts import render
from team.models import Basketball, Player

def home(request):
    context = {
        'player_count': Player.objects.count(),
    }
    return render(request, "base.html", context)