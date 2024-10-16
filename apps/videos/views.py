from django.shortcuts import render
from ..footer.utils import getContact, getAllInformations 
from .models import Video, Category, PageDescription

def videos(request):
    videos = Video.objects.all()
    categorys = Category.objects.all()
    pageDescription = PageDescription.objects.first();

    context = {
        'footerContact': getContact(),
        'footerInformations': getAllInformations(),
        'videos': videos,
        'categorys': categorys,
        'pageDescription': pageDescription,
    }
    return render(request, 'videos.html', context) 
