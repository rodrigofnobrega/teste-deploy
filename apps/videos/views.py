from django.shortcuts import render
from ..footer.models import Contact, Information 
from .models import Video

def videos(request):
    footerContacts = Contact.objects.all()
    footerInformations = Information.objects.all()
    videos = Video.objects.all()

    context = {
        'footerContacts': footerContacts,
        'footerInformations': footerInformations,
        'videos': videos,
    }
    return render(request, 'videos.html', context) 
