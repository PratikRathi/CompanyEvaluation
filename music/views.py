# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Sectors
from django.shortcuts import render, get_object_or_404

def index(request):
    all_sectors = Sectors.objects.all()
    return render(request,'music/index1.html' ,{'all_sectors' : all_sectors} )

def fmcg(request):
    return render(request,'music/comparison.html' ,{} )


def details(request, sector_id):
    sector = get_object_or_404(Sectors,pk = sector_id)
    return render(request, 'music/detail.html', {'sector' : sector} )
