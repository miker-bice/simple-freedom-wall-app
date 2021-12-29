from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add_confession', views.add_confession, name='add-confession'),
    path('confession/<int:item_id>', views.confession, name='confession-detail'),
    path('add_comment', views.add_comment, name='add-comment'),
]
