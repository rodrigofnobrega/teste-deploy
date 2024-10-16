from .models import Contact, Information

def getContact():
    return Contact.objects.first()

def getAllInformations():
    return Information.objects.all()