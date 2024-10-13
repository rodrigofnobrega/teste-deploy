from django.shortcuts import render, redirect
from ..footer.models import Contact, Information 
from .models import Team

def redirect_to_home(request):
    return redirect('home')

def home(request):
    footerContacts = Contact.objects.all()
    footerInformations = Information.objects.all()
    team = Team.objects.all()

    context = {
        'footerContacts': footerContacts,
        'footerInformations': footerInformations,
        'team': team,
    }
    return render(request, 'home.html', context)
