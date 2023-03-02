from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    url = "http://127.0.0.1:8000/"
    return render(request,'index.html')

def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        return render(request,'index.html',{'data':data})
    else:
        return render(request,'index.html')