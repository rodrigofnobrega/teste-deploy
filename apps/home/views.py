from django.shortcuts import render, redirect
from ..footer.utils import getAllContacts, getAllInformations 
from .models import TopDescH, Team, Tool, Button

def redirect_to_home(request):
    return redirect('home')

def home(request):
    topDescH = TopDescH.objects.first()
    team = Team.objects.all()
    tools = Tool.objects.all()
    buttons = Button.objects.all()

    context = {
        'footerContacts': getAllContacts(),
        'footerInformations': getAllInformations(),
        'team': team,
        'tools': tools,
        'topDescH': topDescH,
        'buttons': buttons, 
    }
    return render(request, 'home.html', context)
