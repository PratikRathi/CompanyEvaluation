# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Sectors
from django.shortcuts import render, get_object_or_404

def index(request):
    all_sectors = Sectors.objects.all()
    return render(request,'music/music_main.html' ,{'all_sectors' : all_sectors} )

def fmcg(request):
    #!/usr/bin/env python
# coding: utf-8

    import pandas as pd
    df=pd.read_csv('music/Compare - Sheet1.csv')
    df = df.set_index('Unnamed: 0') 
    df.loc['Sector'] = df.mean()
    df1 = pd.read_csv('music/Comparison_input - Sheet1.csv')
    names = list(df.index)
    pe = {}
    ev={}
    curr_ratio={}
    div_share = {}
    pbdit = {}
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

    y = list(df['Dividend / Share(Rs.)'])
    for i in range(0,len(names)):
        div_share[names[i]]=y[i]

    y = list(df['PBDIT/Share (Rs.)'])
    for i in range(0,len(names)):
        pbdit[names[i]]=y[i]

    y = list(df['Price/BV (X)'])
    for i in range(0,len(names)):
        p_bv[names[i]]=y[i]

    y = list(df['Asset Turnover Ratio (%)'])
    for i in range(0,len(names)):
        asstr[names[i]]=y[i]
        
        
        
    pe['Your Company'] = float(df1['PE Ratio'])
    ev['Your Company'] = float(df1['EV/EBITDA (X)'])
    curr_ratio['Your Company'] = float(df1['Current Ratio (X)'])
    div_share['Your Company'] = float(df1['Dividend / Share(Rs.)'])
    pbdit['Your Company'] = float(df1['PBDIT/Share (Rs.)'])
    p_bv['Your Company'] = float(df1['Price/BV (X)'])
    asstr['Your Company'] = float(df1['Asset Turnover Ratio (%)'])


    diff_sector_ratio = {}
    diff_sector_ratio['PERatio'] = ((float(df1['PE Ratio'])-df['PE Ratio']['Sector'])/df['PE Ratio']['Sector'])*100
    diff_sector_ratio['EVEBITDA'] = ((float(df1['EV/EBITDA (X)'])-df['EV/EBITDA (X)']['Sector'])/df['EV/EBITDA (X)']['Sector'])*100
    diff_sector_ratio['Current Ratio (X)'] = float(df1['Current Ratio (X)'])-df['Current Ratio (X)']['Sector']
    diff_sector_ratio['DividendShare'] = ((float(df1['Dividend / Share(Rs.)'])-df['Dividend / Share(Rs.)']['Sector'])/df['Dividend / Share(Rs.)']['Sector'])*100
    diff_sector_ratio['PBDIT/Share (Rs.)'] = float(df1['PBDIT/Share (Rs.)'])-df['PBDIT/Share (Rs.)']['Sector']
    diff_sector_ratio['Price/BV (X)'] = float(df1['Price/BV (X)'])-df['Price/BV (X)']['Sector']
    diff_sector_ratio['AssetTurnoverRatio'] = ((float(df1['Asset Turnover Ratio (%)'])-df['Asset Turnover Ratio (%)']['Sector'])/df['Asset Turnover Ratio (%)']['Sector'])*100
    intercept=-21.64410443
    div_var=-0.1918819996
    PBDIT_var=0.1364471059
    astr_var=0.2951034307
    ev_var=0.729999005
    total = intercept + div_var*float(df1['Dividend / Share(Rs.)']) + PBDIT_var*float(df1['PBDIT/Share (Rs.)']) + astr_var*float(df1['Asset Turnover Ratio (%)']) + ev_var * float(df1['EV/EBITDA (X)'])
    attractiveness = total - float(df1['PE Ratio'])
    attractiveness_index = attractiveness/float(df1['PE Ratio'])
    attract_dict = {
        'predicted' : total,
        'actual': float(df1['PE Ratio']),
        'attractiveness' : attractiveness,
        'attractiveness_index' : attractiveness_index
    }
    return render(request,'music/excel1.html' ,{'asstr' : asstr, 'p_bv' : p_bv, 'pbdit' : pbdit, 'div_share' : div_share, 'curr_ratio': curr_ratio, 'ev' : ev, 'pe' : pe, 'attract_dict' : attract_dict, 'diff_sector_ratio' : diff_sector_ratio} )


def details(request, sector_id):
    sector = get_object_or_404(Sectors,pk = sector_id)
    return render(request, 'music/detail.html', {'sector' : sector} )