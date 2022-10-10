from cmath import exp
from django.shortcuts import render
import json 
import urllib.request,urllib.error
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
           
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a15ea8dfd84147a3e97ccc213ae59b6d').read()
            jason_data= json.loads(res)
            data = {
                'country_code':str(jason_data['sys']['country']),
                'coordinate':str(jason_data['coord']['lon'])+' '+ str(jason_data['coord']['lat']),
                'temp': str(jason_data['main']['temp'])+ '  K',
                'pressure':str(jason_data['main']['pressure']),
                'humidity':str(jason_data['main']['humidity']),}
        except :
            data="Please enter valid country"
        
        
                


            
    else:
        data = {}
        city=''
    if city == '' and data != "Please enter valid country" :
        x="Use the country query to see forecast"
    else:
        x=""
    return render(request, 'index.html', {'city':city, 'data':data,'x':x})


 