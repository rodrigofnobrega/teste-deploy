from .models import Contact, Information

def getAllContacts():
    return Contact.objects.all()

def getAllInformations():
    return Information.objects.all()