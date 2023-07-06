from django.shortcuts import render
import pandas as pd
import datetime as dt
from datetime import date
import os
from django.http import HttpResponse, JsonResponse, Http404
from django.core.files.storage import default_storage


import xlsxwriter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# now = datetime.now()
# today = now.strftime("%d/%m/%Y %H:%M:%S")
# today = now+today
today = date.today()
print(today)


# Create your views here.
def tablesexcel(request):
    df = pd.read_excel('C:/Users/hp/Documents/project/myproject/myapp/static/data.xlsx')
    dts = df['date'].unique()
    dts = dts.astype(str).tolist() 
    dts = pd.to_datetime(dts)   
    sources = df['source'].unique().tolist()
    types = df['type'].unique().tolist()
    optitarget = df['optimisation_target'].unique().tolist()

    type = request.POST.get('type')
    source = request.POST.get('source')
    target = request.POST.get('target')
    from_date = request.POST.get('from_date')
    to_date = request.POST.get('to_date')
    dfs = df
    dfs = dfs.fillna(0)
    if request.POST.get('type'):
        if source != "":
            dfs= dfs.loc[(df['source'] == source)]
    if request.POST.get('source'):
        if type != "":
            dfs= dfs.loc[(df['type'] == type)]
    if request.POST.get('target'):
        if target != "":
            dfs= dfs.loc[(df['optimisation_target'] == target)]
        if request.POST.get('from_date'):
            if request.POST.get('to_date'):
                dfs= dfs.loc[(df['date'].astype('string') >= from_date) & (df['date'].astype('string') <= to_date)]   
    dates= dfs['date'].astype(str).to_list()
    date = sorted(dates)    
    var = dfs.to_dict(orient='list')
        
    print(dfs.to_excel(f'C:/Users/hp/Documents/project/myproject/myapp/static/dummy.xlsx',index=False))
    
       
     

        
    return render(request,'tablesexcel.html',{'var':var,'date':date,'dts':dts,'df':dfs,'sources':sources,'types':types,'optitarget':optitarget, 'from_date': from_date, 
                                              'to_date': to_date, 'target': target, 'type': type, 'source': source,})


def temp_export(request):
    filename = BASE_DIR + f"/static/dummy.xlsx"
    print(filename)
    if os.path.exists(filename):
        with open(filename, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
            return response
    return render(request, 'tablesexcel.html', {'msg': 'Something went wrong; Try Again'})