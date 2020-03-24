from django.shortcuts import render
from .models import user
from rest_framework.decorators import api_view
from Serializers.authentication import authenticationSerializer, isValidUser
from Serializers.isValid import isValid, isValidSerializer
from rest_framework.response import Response


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


@api_view(['GET'])
def login(request):
    username = request.query_params.get('username')
    password = request.query_params.get('password')
    if user.objects.get(username=username, password=password) is not None:
        return Response(authenticationSerializer(isValidUser(True)).data)
    else:
        return Response(authenticationSerializer(isValidUser(False)).data)


@api_view(['POST'])
def createUser(request):
    username = request.query_params.get('username')
    password = request.query_params.get('password')
    email = request.query_params.get('email')
    firstName = request.query_params.get('firstName')
    lastName = request.query_params.get('lastName')
    thisUser = user(username=username, password=password, email=email, firstName=firstName, lastName=lastName)
    thisUser.save()
    return Response(isValidSerializer(isValid(True)).data)
