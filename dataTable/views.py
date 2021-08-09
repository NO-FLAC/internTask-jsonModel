from django.shortcuts import render
from django.http import HttpResponse

import json

with open('stock_market_data.json') as dataSet:
    data = json.load(dataSet)

# Create your views here.

def mainPage(resquest):
    return render(resquest,'Tables/main.html', {'data':data})



