"""django3base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.urls import path
from demo.views import DataListView
from utr5.views import UTR5ListView
from cds.views import codon_optimize, get_seq, eq_random_seq, prob_random_seq, dnachisel_seq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('demo/', DataListView.as_view(), name='demo'),
    path('plasmid/', TemplateView.as_view(template_name='plasmid.html'), name='plasmid'),
    path('utr5/', UTR5ListView.as_view(), name='utr5'),
    path('cds/', codon_optimize, name='cds'),
    path('utr3/', TemplateView.as_view(template_name='utr3.html'), name='utr3'),
    path('struc/', TemplateView.as_view(template_name='struc.html'), name='struc'),
    path('pdb/', TemplateView.as_view(template_name='pdb_structure_template.html'), name='pdb'),
    path('cds/seq', get_seq, name='seq'),
    path('cds/eq_random_seq', eq_random_seq, name='eq_random_seq'),
    path('cds/prob_random_seq', prob_random_seq, name='prob_random_seq'),
    path('cds/dnachisel_seq', dnachisel_seq, name='dnachisel_seq'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
