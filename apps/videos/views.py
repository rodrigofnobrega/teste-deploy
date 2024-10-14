from django.shortcuts import render
from ..footer.utils import getAllContacts, getAllInformations 
from .models import Video

def videos(request):
    videos = Video.objects.all()

    context = {
        'footerContacts': getAllContacts(),
        'footerInformations': getAllInformations(),
        'videos': videos,
    }
    return render(request, 'videos.html', context) 
