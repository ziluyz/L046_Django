from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('plankton', views.plankton, name='plankton'),
    path('crabs', views.crabs, name='crabs'),
    path('octopus', views.octopus, name='octopus'),
    path('bivalves', views.bivalves, name='bivalves'),
]