from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=45ca8733087d9bd7449f231df1f2e577').read()
        json_data = json.loads(res)
        data = {
            "name" : str(json_data['name']),
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : 'Longitude : ' + str(json_data['coord']['lon']) + ' ' + 'Latitude : '+str(json_data['coord']['lat']),
            "temprature" : str(int(abs(json_data['main']['temp'])-(273.15)))+'°C',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
            "description" : str(json_data['weather'][0]['description']),
         }

    else:
        data = {}
    return render(request, 'index.html', data)
