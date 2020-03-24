from django.shortcuts import render
from .models import user, tryout, criterion
from rest_framework.decorators import api_view
from Serializers.checkUser import userID, userIDSerializer
from Serializers.isValid import isValid, isValidSerializer
from Serializers.listTryouts import tryoutForList, listTryoutsSerializer
from Serializers.listCriteria import criterionForList, listCriteriaSerializer
from rest_framework.response import Response


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


@api_view(['GET'])
def checkUser(request):
    username = request.query_params.get('username')
    password = request.query_params.get('password')
    thisUser = user.objects.get(username=username, password=password)
    if thisUser is not None:
        return Response(userIDSerializer(userID(thisUser.id)).data)
    else:
        return Response(userIDSerializer(userID(0)).data)


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


@api_view(['POST'])
def createTryout(request):
    username = request.query_params.get('username') # USE THIS LATER FOR INDIVIDUAL TRYOUT LISTS
    thisUser = user.objects.get(username=username)
    tryoutName = request.query_params.get('tryoutName')
    thisTryout = tryout(admin=thisUser, name=tryoutName)
    thisTryout.save()
    i = 1
    criterionName = request.query_params.get('criterion1')
    while criterionName is not None:
        thisCriterion = criterion(tryout=thisTryout, name=criterionName)
        thisCriterion.save()
        i += 1
        criterionName = request.query_params.get('criterion' + str(i))
    return Response(isValidSerializer(isValid(True)).data)


@api_view(['POST'])
def deleteTryout(request):
    tryoutID = request.query_params.get('tryoutID')
    thisTryout = tryout.objects.get(id=tryoutID)
    thisTryout.delete()
    return Response(isValidSerializer(isValid(True)).data)


@api_view(['GET'])
def listTryouts(request):
    userID = request.query_params.get('userID')
    thisUser = user.objects.get(id=userID)
    tryoutIDs = tryout.objects.filter(admin=thisUser).values_list('id', flat=True)
    tryoutNames = tryout.objects.filter(admin=thisUser).values_list('name', flat=True)
    return Response(listTryoutsSerializer(tryoutForList(tryoutIDs, tryoutNames)).data)


@api_view(['GET'])
def listCriteria(request):
    tryoutID = request.query_params.get('tryoutID')
    thisTryout = tryout.objects.get(id=tryoutID)
    criteriaList = criterion.objects.filter(tryout=thisTryout).values_list('name', flat=True)
    return Response(listCriteriaSerializer(criterionForList(criteriaList)).data)