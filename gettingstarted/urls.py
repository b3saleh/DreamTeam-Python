from django.urls import path, include
from hello import views

urlpatterns = [
    path("", views.index, name='index'),
    path('checkUser/', views.checkUser, name='Check User'),
    path('createUser/', views.createUser, name='Create User'),
    path('createTryout/', views.createTryout, name='Create a new Tryout'),
    path('deleteTryout/', views.deleteTryout, name='Delete tryout by ID'),
    path('listTryouts/', views.listTryouts, name='List all Tryouts for a given user'),
    path('listCriteria/', views.listCriteria, name='List Criteria for a given Tryouts'),
]
