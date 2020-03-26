from django.shortcuts import render
from .models import user, tryout, criterion, player, session
from rest_framework.decorators import api_view
from Serializers.checkUser import userID, userIDSerializer
from Serializers.isValid import isValid, isValidSerializer
from Serializers.listTryouts import tryoutForList, listTryoutsSerializer
from Serializers.listSessions import sessionForList, listSessionsSerializer
from Serializers.listCriteria import criterionForList, listCriteriaSerializer
from Serializers.listPlayers import playerForList, listPlayersSerializer
from rest_framework.response import Response
from django.db.models import Q


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
    userID = request.query_params.get('userID') # USE THIS LATER FOR INDIVIDUAL TRYOUT LISTS
    thisUser = user.objects.get(id=userID)
    tryoutName = request.query_params.get('tryoutName')
    thisTryout = tryout(admin=thisUser, name=tryoutName)
    thisTryout.save()
    criteriaList = request.GET.getlist('criteria')
    for criterionName in criteriaList:
        thisCriterion = criterion(tryout=thisTryout, name=criterionName)
        thisCriterion.save()
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
    allTryouts = tryout.objects.filter(Q(admin=thisUser) | Q(executives=thisUser))
    tryoutIDs = []
    tryoutNames = []
    for thisTryout in allTryouts:
        tryoutIDs.insert(len(tryoutIDs), thisTryout.id)
        tryoutNames.insert(len(tryoutNames), thisTryout.name)
    return Response(listTryoutsSerializer(tryoutForList(tryoutIDs, tryoutNames)).data)


@api_view(['GET'])
def listCriteria(request):
    tryoutID = request.query_params.get('tryoutID')
    thisTryout = tryout.objects.get(id=tryoutID)
    criteriaList = criterion.objects.filter(tryout=thisTryout)
    criteriaNames = []
    for thisCriterion in criteriaList:
        criteriaNames.insert(len(criteriaNames), thisCriterion.name)
    return Response(listCriteriaSerializer(criterionForList(criteriaNames)).data)


@api_view(['POST'])
def addExecs(request):
    tryoutID = request.query_params.get('tryoutID')
    execEmails = request.GET.getlist('execEmails')
    thisTryout = tryout.objects.get(id=tryoutID)
    for thisEmail in execEmails:
        thisExec = user.objects.get(email=thisEmail)
        thisTryout.executives.add(thisExec)
    return Response(isValidSerializer(isValid(True)).data)

@api_view(['POST'])
def addSession(request):
    tryoutID = request.query_params.get('tryoutID')
    thisTryout = tryout.objects.get(id=tryoutID)
    startTime = request.query_params.get('startTime')
    endTime = request.query_params.get('endTime')
    location = request.query_params.get('location')
    thisSession = session(tryout=thisTryout, startTime=startTime, endTime=endTime, location=location)
    thisSession.save()
    return Response(isValidSerializer(isValid(True)).data)

@api_view(['POST'])
def deleteSession(request):
    sessionID = request.query_params.get('sessionID')
    thisSession = session.objects.get(id=sessionID)
    thisSession.delete()
    return Response(isValidSerializer(isValid(True)).data)

@api_view(['GET'])
def listSessions(request):
    tryoutID = request.query_params.get('tryoutID')
    thisTryout = tryout.objects.get(id=tryoutID)
    allSessions = session.objects.filter(tryout=thisTryout)
    sessionIDs = []
    sessionStarts = []
    for thisSession in allSessions:
        sessionIDs.insert(len(sessionIDs), thisSession.id)
        sessionStarts.insert(len(session), thisSession.startTime)
    return Response(listSessionsSerializer(sessionForList(sessionIDs,sessionStarts)).data)


@api_view(['POST'])
def createPlayer(request):
    tryoutID = request.query_params.get('tryoutID')
    firstName = request.query_params.get('firstName')
    lastName = request.query_params.get('lastName')
    email = request.query_params.get('email')
    thisTryout = tryout.objects.get(id=tryoutID)
    thisPlayer = player(tryout=thisTryout, firstName=firstName, lastName=lastName, email=email)
    thisPlayer.save()
    return Response(isValidSerializer(isValid(True)).data)

@api_view(['POST'])
def deletePlayer(request):
    playerID = request.query_params.get('playerID')
    thisPlayer = player.objects.get(id=playerID)
    thisPlayer.delete()
    return Response(isValidSerializer(isValid(True)).data)

@api_view(['GET'])
def listPlayers(request):
    tryoutID = request.query_params.get('tryoutID')
    thisTryout = tryout.objects.get(id=tryoutID)
    allPlayers = player.objects.filter(tryout=thisTryout)
    playerIDs = []
    playerFirstNames = []
    playerLastNames = []
    for thisPlayer in allPlayers:
        playerIDs.insert(len(playerIDs), thisPlayer.id)
        playerFirstNames.insert(len(playerFirstNames), thisPlayer.firstName)
        playerLastNames.insert(len(playerLastNames), thisPlayer.lastName)
    return Response(listPlayersSerializer(playerForList(playerIDs,playerFirstNames,playerLastNames)).data)