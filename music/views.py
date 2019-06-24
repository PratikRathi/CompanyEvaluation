# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Sectors
from django.shortcuts import render, get_object_or_404

def index(request):
    all_sectors = Sectors.objects.all()
    return render(request,'music/index1.html' ,{'all_sectors' : all_sectors} )

def fmcg(request):
    #!/usr/bin/env python
# coding: utf-8

    import pandas as pd
    df=pd.read_csv('/home/rahil/Desktop/FInal Project/Compare - Sheet1.csv')
    df = df.set_index('Unnamed: 0') 
    df.loc['Sector'] = df.mean()
    df1 = pd.read_csv('/home/rahil/Desktop/FInal Project/Comparison_input - Sheet1.csv')
    names = list(df.index)
    pe = {}
    ev={}
    curr_ratio={}
    q_ratio = {}
    itr = {}
    p_bv = {}
    asstr = {}
    y = list(df['PE Ratio'])
    for i in range(0,len(names)):
        pe[names[i]]=y[i]

    y = list(df['EV/EBITDA (X)'])
    for i in range(0,len(names)):
        ev[names[i]]=y[i]

    y = list(df['Current Ratio (X)'])
    for i in range(0,len(names)):
        curr_ratio[names[i]]=y[i]

    y = list(df['Quick Ratio (X)'])
    for i in range(0,len(names)):
        q_ratio[names[i]]=y[i]

    y = list(df['Inventory Turnover Ratio (X)'])
    for i in range(0,len(names)):
        itr[names[i]]=y[i]

    y = list(df['Price/BV (X)'])
    for i in range(0,len(names)):
        p_bv[names[i]]=y[i]

    y = list(df['Asset Turnover Ratio (%)'])
    for i in range(0,len(names)):
        asstr[names[i]]=y[i]
        
        
        
    pe['Your Company'] = float(df1['PE Ratio'])
    ev['Your Company'] = float(df1['EV/EBITDA (X)'])
    curr_ratio['Your Company'] = float(df1['Current Ratio (X)'])
    q_ratio['Your Company'] = float(df1['Quick Ratio (X)'])
    itr['Your Company'] = float(df1['Inventory Turnover Ratio (X)'])
    p_bv['Your Company'] = float(df1['Price/BV (X)'])
    asstr['Your Company'] = float(df1['Asset Turnover Ratio (%)'])
    return render(request,'music/comparison.html' ,{'asstr' : asstr, 'p_bv' : p_bv, 'itr' : itr, 'q_ratio' : q_ratio, 'curr_ratio': curr_ratio, 'ev' : ev, 'pe' : pe} )


def details(request, sector_id):
    sector = get_object_or_404(Sectors,pk = sector_id)
    return render(request, 'music/detail.html', {'sector' : sector} )
