from django.shortcuts import render
from ..footer.utils import getAllContacts, getAllInformations 
from .models import TopDesc, Material, CategoryP

def parents(request):
    top_descs = TopDesc.objects.all()
    drawings_and_cards = Material.objects.all()
    categories = CategoryP.objects.all()
    
    context = {
        'top_descs': top_descs,
        'drawings_and_cards': drawings_and_cards,
        'categories': categories,
        'footerContacts': getAllContacts(),
        'footerInformations': getAllInformations(),
    }
    return render(request, 'parents.html', context)
