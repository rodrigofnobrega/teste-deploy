from django.shortcuts import render, redirect
from ..footer.models import Contact, Information 

def redirect_to_home(request):
    return redirect('home')

def home(request):

    footerContacts = Contact.objects.all()
    footerInformations = Information.objects.all()

    context = {
        'footerContacts': footerContacts,
        'footerInformations': footerInformations,
    }
    return render(request, 'home.html', context)
