from django.shortcuts import render, redirect
from ..footer.utils import getAllContacts, getAllInformations 
from .models import TopDescH, Team, Tool, Button, PlatformDesc, ForumItens, SupportMaterial

def redirect_to_home(request):
    return redirect('home')

def home(request):
    topDescH = TopDescH.objects.first()
    platFormDesc = PlatformDesc.objects.first()
    forumItens = ForumItens.objects.all()
    team = Team.objects.all()
    tools = Tool.objects.all()
    button = Button.objects.first()
    supportMaterials = SupportMaterial.objects.all()

    context = {
        'footerContacts': getAllContacts(),
        'footerInformations': getAllInformations(),
        'team': team,
        'tools': tools,
        'topDescH': topDescH,
        'platformDesc': platFormDesc,
        'button': button,
        'forumItens': forumItens, 
        'supportMaterials': supportMaterials, 
    }
    return render(request, 'home.html', context)
