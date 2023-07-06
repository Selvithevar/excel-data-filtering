from django.shortcuts import render
import pandas as pd

# Create your views here.
# def tablesexcel(request):
df = pd.read_excel('C:/Users/hp/Documents/project/myproject/myapp/static/data.xlsx')
# for k,v in df.items():
#     source = v['source'].sum()
#     print(source)
# var = df['source'].str.split(expand=True).stack().value_counts()
# var1 = df['attributed_conversions'].astype(int).value_counts()
# print(var1)
type = 'baseline'
source = 'direct'
target = 'revenue'
from_date = '22-03-2022'
to_date = '25-03-2022'
dfs= df.loc[(df['source']==source) & (df['type']==type) & (df['optimisation_target']==target)]
# dfs = df.loc(df['source']==source)
print(dfs,'<--df')

    # var = df.groupby(type)
    # print(var,'<---var')


    # sources = df['source'].unique().tolist()
    # types = df['type'].unique().tolist()
    # optitarget = df['optimisation_target'].unique().tolist()