from django.shortcuts import render
from ..footer.models import Contact, Information 

def home(request):

    footerContacts = Contact.objects.all()
    footerInformations = Information.objects.all()

    context = {
        'footerContacts': footerContacts,
        'footerInformations': footerInformations,
    }
    return render(request, 'home.html', context)
