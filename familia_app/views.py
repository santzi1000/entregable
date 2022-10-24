#from multiprocessing import context
from django.shortcuts import render

from familia_app.models import Familiar

def familiars(request):
    familiars = Familiar.objects.all()

    context_dict = {"familiars": familiars}

    return render(
        request=request,
        context=context_dict,
        template_name="familia_app/familiar_list.html",

    )
