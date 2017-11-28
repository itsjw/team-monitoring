import requests
from django.http import HttpResponse


def get_data_zoxon(request):
    url = 'http://192.168.20.171:8001/api/v1/zoxon470/'
    zoxon = requests.get(url).json()
    return HttpResponse(zoxon)




