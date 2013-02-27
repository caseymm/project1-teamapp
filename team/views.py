# Create your views here.
from django.shortcuts import render
from team.models import Basketball, Football, Baseball

def home(request):
    context = {
        'player_count': Basketball.objects.count(),
    }
    return render(request, "base.html", context)