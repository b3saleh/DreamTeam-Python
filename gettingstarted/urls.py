from django.urls import path, include
from hello import views

urlpatterns = [
    path("", views.index, name='index'),
    path('login/', views.login, name='login'),
    path('createUser/', views.createUser, name='createUser'),
]
