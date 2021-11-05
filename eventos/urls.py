from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView),
    path('crear-rifa/', createView),

]



