# Create your views here.
from team.models import Basketball, Football, Baseball
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {
        'player_count': Basketball.objects.count(),
    }
    return render(request, "team/home.html", context)

def basketball(request):
    #basketball = Basketball.objects.order_by('?')[0]
    basketball = get_object_or_404(Basketball, id=pk)
    return render(request, "team/basketball.html", {'player': player})

def basketballList(request):
    basketball_list = Basketball.objects.all()
    paginator = Paginator(basketball_list, 25)
    page = request.GET.get('page')
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        players = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        players = paginator.page(paginator.num_pages)
    
    return render(request, 'team/basketball_list.html', {"players": players})
