from django.shortcuts import render
from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime
from django.shortcuts import redirect


# Create your views here.
def index(request):
    response = {}
    return render(request, 'index.html', response)

def answer(request,answer = None):
    response={}
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: 
        dumps(x).encode('utf-8'))

    now = datetime. now()
    answer = request.POST['action']
    name = request.POST['name']
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    data = {'timestamp':timestamp, 'answer' : int(answer), 'name':name}
    producer.send('demo_test1', value=data)
    sleep(1)
    return redirect('/success/')

def success(request):
    response = {}
    return render(request, 'success.html', response)