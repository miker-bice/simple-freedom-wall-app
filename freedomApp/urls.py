from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('addConfession', views.addConfessionView, name='add-confession'),
    path('new_page', views.new_page, name='new-page'),
]
