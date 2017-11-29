from django.conf.urls import url
from api.views import get_data_zoxon


urlpatterns = [
    url(r'^get_data_zoxon', get_data_zoxon, name='zoxon')
]
