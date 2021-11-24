from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView),
    path('crear-rifa/', createView),
    path('rifa/<int:id>/', rifaView),
    path('ver-rifa/<int:id>/', verRifa),

]



