from django.shortcuts import render

# Create your views here.
from utr5.models import UTR5
from django.views.generic.list import ListView


class UTR5ListView(ListView):
    model = UTR5
