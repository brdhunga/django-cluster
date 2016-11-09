import json

from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from django.conf import settings 

from .models import DjangoCluster
from .model_utils import scale_models


WIDTH = settings.DC_SVG_WIDTH
HEIGHT = settings.DC_SVG_HEIGHT 


def home_view(request):
    return render(request, 'index.html',
        {'height' : HEIGHT, 'width': WIDTH}
        )

def train_view(request):
    obj_ = scale_models()
    json_ = json.dumps(obj_)
    DjangoCluster.objects.create()


def json_view(request):
    obj_ = scale_models()
    json_ = json.dumps(obj_)
    print(type(json_))
    return JsonResponse(obj_, safe=False)
