# Create your views here.
from team.models import Basketball, Football, Baseball, Coach
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from chartit import PivotDataPool, PivotChart

def home(request):
    context = {
        'player_count': Basketball.objects.count(),
    }
    return render(request, "team/home.html", context)

def basketball(request, pk):
    player = get_object_or_404(Basketball, id=pk)
    coaches = Coach.objects.all()
    coach_count = len(coaches)
    if pk <= coach_count:
        coach = get_object_or_404(Coach, id=pk)
    else:
        coach = ""
        
        
    context = {
        'player': player,
        'coach': coach,
    }
    return render(request, "team/basketball.html", context)
    

def basketballList(request):
    basketball_list = Basketball.objects.all()
    coaches = Coach.objects.all()
    paginator = Paginator(basketball_list, 25)
    page = request.GET.get('page')
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
         #If page is not an integer, deliver first page
        players = paginator.page(1)
        
    except EmptyPage:
        #If page is out of range (e.g. 9999), deliver last page of results
        players = paginator.page(paginator.num_pages)

    
    context = {
        'players': players,
        'coaches': coaches,
        
    }
    
    return render(request, 'team/basketball_list.html', context)



