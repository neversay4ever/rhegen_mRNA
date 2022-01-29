from django.shortcuts import render

# Create your views here.
from utr5.models import UTR5
from django.views.generic.list import ListView


from django.utils.html import format_html
from django.utils.safestring import mark_safe

class UTR5ListView(ListView):
    model = UTR5


from django.http import HttpResponse,JsonResponse
import json

def index(request):
    data={
        'name':'zhangsan',
        'age':18,
    }
    return HttpResponse(json.dumps(data))

def json_anno(request):
    id = request.GET.get('id')
    data = UTR5.objects.filter(utr5_id=id).values()[0]
    data.get('utr5_id')
    data = {
        'id':data.get('utr5_id'),
        'note': data.get('utr5_note'),
        'seq': data.get('utr5_seq'),
        'anno': data.get('utr5_anno')
    }
    return JsonResponse(json.dumps(data),safe=False)

    