from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import PeakLocation
from django.template import loader
# Create your views here.

def index(request):
    peaklocation_list = PeakLocation.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'peaklocation_list': peaklocation_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, peaklocation_id):
    peaklocation = get_object_or_404(PeakLocation, pk=peaklocation_id)
    return render(request, 'polls/detail.html', {'peaklocation': peaklocation})
