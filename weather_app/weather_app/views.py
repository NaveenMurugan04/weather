import json
from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
import requests



def home(request):
  
  template = loader.get_template('home.html')
 
  

  
  return HttpResponse(template.render())

def fetch_weathers_list():
     req_url= "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25"
     return requests.get(req_url)
