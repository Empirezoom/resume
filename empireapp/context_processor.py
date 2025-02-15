from .models import *





def general(request):
    c_profile = CompanyProfile.objects.get(pk=1)
    info = About.objects.get(pk=1)
    category=Category.objects.all()

    context = {
        'c_profile': c_profile,
        'info': info,
        'category': category,



    }

    return context