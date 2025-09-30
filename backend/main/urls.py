from django.urls import path 
from . import views


#api/pantry
urlpatterns = [
    path('home', views.home, name='main'),
    path('data', views.get_data, name='get_data'),
    path('add', views.add_ingredient, name='add_ingredient'),
]