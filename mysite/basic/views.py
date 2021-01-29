from django.shortcuts import render

# Create your views here.
def home(request):
    import requests 
    import json


    #

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC&tsyms=USD,EUR")
    price = json.loads(price_request.content)
   

    #https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR
    #https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR


    #
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)


    return render(request,'home.html', {'api':api, 'price':price})
    