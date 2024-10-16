from django.shortcuts import render
from ..footer.utils import getContact, getAllInformations 
from .models import Video, Category, PageDescription, TopImageVideo1, TopImageVideo2, TopImageVideo3, TopImageVideo4, TopImageVideo5, TopImageVideo6, TopImageVideo7

def videos(request):
    videos = Video.objects.all()
    categorys = Category.objects.all()
    pageDescription = PageDescription.objects.first();

    images_1 = TopImageVideo1.objects.all()
    images_2 = TopImageVideo2.objects.all()
    images_3 = TopImageVideo3.objects.all()
    images_4 = TopImageVideo4.objects.all()
    images_5 = TopImageVideo5.objects.all()
    images_6 = TopImageVideo6.objects.all()
    images_7 = TopImageVideo7.objects.all()

    context = {
        'footerContact': getContact(),
        'footerInformations': getAllInformations(),
        'videos': videos,
        'categorys': categorys,
        'pageDescription': pageDescription,
        'images_1': images_1,
        'images_2': images_2,
        'images_3': images_3,
        'images_4': images_4,
        'images_5': images_5,
        'images_6': images_6,
        'images_7': images_7,
    }
    return render(request, 'videos.html', context) 
