# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import openpyxl
from django.shortcuts import render, render_to_response

def index(request):
    return render(request, "index.html", {})

def excel_index(request):
    if "GET" == request.method:
        return render(request, "excel.html", {})
    else:
        excel_file = request.FILES["excel_file"]
        df1 = openpyxl.load_workbook(excel_file)
        df = df1["Sheet1"]
        current_ratio = []
        quick_ratio = []
        debt_equity = []
        current_ratio.append('current_ratio')
        quick_ratio.append('quick_ratio')
        debt_equity.append('debt_equity')

        shareholders = []
        Total_Assets = []
        Total_Liabilities = []
        cash = []
        investments = []
        current_assets = []
        receivables = []

        max_column = df.max_column
        for i in range(1, max_column + 1):
            shareholders.append(df.cell(row=6, column=i))
            Total_Assets.append(df.cell(row=35, column=i))
            Total_Liabilities.append(df.cell(15, i))
            cash.append(df.cell(32, i))
            investments.append(df.cell(29, i))
            current_assets.append(df.cell(34, i))
            receivables.append(df.cell(31, i))

        shareholders = list(shareholders)
        Total_Assets = list(Total_Assets)
        # Total_Liabilities = list(df.iloc[14])
        # cash = list(df.iloc[31])
        # investments = list(df.iloc[28])
        # current_assets = list(df.iloc[33])
        # receivables = list(df.iloc[30])

        cash.pop(0)
        investments.pop(0)
        current_assets.pop(0)
        receivables.pop(0)
        Total_Assets.pop(0)
        Total_Liabilities.pop(0)
        shareholders.pop(0)

        x_quick = cash + investments + current_assets + receivables
        print(x_quick)
        for i in range(0, len(Total_Liabilities)):
            current_ratio.append(float(Total_Assets[i].value) / float(Total_Liabilities[i].value))
            x_quick[i] = float(cash[i].value) + float(investments[i].value) + float(current_assets[i].value) + float(
                receivables[i].value)
            quick_ratio.append(float(x_quick[i]) / float(Total_Liabilities[i].value))
            debt_equity.append(float(Total_Liabilities[i].value) / float(shareholders[i].value))
        print(current_ratio)
        print(quick_ratio)

        excel_data = list()

        excel_data.append(current_ratio)
        excel_data.append(quick_ratio)
        excel_data.append(debt_equity)
        print(len(excel_data))

        df2 = df1.create_sheet('Financial_Ratios')
        for row in excel_data:
            df2.append(row)
        df1.save(excel_file)

        print(df2.max_column)
        l3 = []
        current_ratio_perc = []
        l3.append(['current_ratio', 'quick_ratio', 'debt_equity'])
        excel_data = list(excel_data)
        for i in range(1, df2.max_column - 1):
            l = []
            l1 = []
            [l.append(excel_data[p][i]) for p in range(0, 3)]
            [l1.append(excel_data[k][i + 1]) for k in range(0, 3)]
            for j in range(0, len(l)):
                if (l1[j] == 0 or l[j] == 0):
                    l[j] = 0
                else:
                    l[j] = ((l[j] - l1[j]) / l1[j]) * 100
            l3.append(l)
            current_ratio_perc = [[l3[j][i] for j in range(len(l3))] for i in range(len(l3[0]))]




        # made a dictionary and added key name with a list value
        ratio_data = {"current_ratio": [], "quick_ratio": [], "debt_equity": [],"current_ratio_perc" : []}
        i=1
        name = 0

        # we have a number of lists in excel_data and this function is
        # converting it into lists of each key based on list number
        for row in excel_data:
            i=0
            name=name+1
            for cell in row:
               if(i==0):
                   i=i+1
               elif(name==1):
                   ratio_data['current_ratio'].append(cell)
               elif(name==2):
                   ratio_data['quick_ratio'].append(cell)
               elif (name==3):
                   ratio_data['debt_equity'].append(cell)
        for row in current_ratio_perc:
            ratio_data['current_ratio_perc'].append(row)

        # passing a dictionary to the template
        return render(request, 'excel.html', ratio_data)



