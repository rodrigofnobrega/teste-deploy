from django.shortcuts import render, redirect
from ..footer.utils import getAllContacts, getAllInformations 
from .models import Team, Tool

def redirect_to_home(request):
    return redirect('home')

def home(request):
    team = Team.objects.all()
    tools = Tool.objects.all()

    context = {
        'footerContacts': getAllContacts(),
        'footerInformations': getAllInformations(),
        'team': team,
        'tools': tools,
    }
    return render(request, 'home.html', context)
