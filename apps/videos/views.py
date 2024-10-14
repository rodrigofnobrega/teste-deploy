from django.shortcuts import render
from ..footer.utils import getAllContacts, getAllInformations 
from .models import Video, Category

def videos(request):
    videos = Video.objects.all()
    categorys = Category.objects.all()

    context = {
        'footerContacts': getAllContacts(),
        'footerInformations': getAllInformations(),
        'videos': videos,
        'categorys': categorys,
    }
    return render(request, 'videos.html', context) 
