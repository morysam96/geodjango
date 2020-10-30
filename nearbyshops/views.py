from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.views import generic
from .models import *

lattitude = 37.3899814
longitude = 46.2296908
user_location = Point(longitude,lattitude,srid=4326)
class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',user_location)).order_by('distance')[0:10]
    template_name = 'index.html'
