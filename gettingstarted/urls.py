from django.urls import path, include
from hello import views

urlpatterns = [
    path("", views.index, name='index'),
    path('checkUser/', views.checkUser, name='Check User'),
    path('getUserInfo/', views.getUserInfo, name='Get User Info'),
    path('createUser/', views.createUser, name='Create User'),
    path('createTryout/', views.createTryout, name='Create a new Tryout'),
    path('deleteTryout/', views.deleteTryout, name='Delete tryout by ID'),
    path('listTryouts/', views.listTryouts, name='List all Tryouts for a given user'),
    path('listCriteria/', views.listCriteria, name='List Criteria for a given Tryouts'),
    path('addExecs/', views.addExecs, name='Give Executives access to a tryout'),
    path('addSession/', views.addSession, name='Add Session for a given tryout'),
    path('deleteSession/', views.deleteSession, name='Delete Session by ID'),
    path('listSessions/', views.listSessions, name='List all Session IDs and start times for a given tryout'),
    path('createPlayer/', views.createPlayer, name='Create new player entry for a given tryout'),
    path('deletePlayer/', views.deletePlayer, name='Delete Player by ID'),
    path('listPlayers/', views.listPlayers, name='List all players for a tryout'),
    path('submitEval/', views.submitEval, name="Evaluation Submission"),
    path('postComment/', views.postComment, name="Posts a comment"),
    path('createTeam/', views.createTeam, name="Create a New Team within a tryout"),
    path('getEvals/', views.getEvals, name="Get Evaluation Info"),
    path('getComments/', views.getComments,  name="Gets comments for a User"),
    path('getTeamAverages/', views.getTeamAverages, name="Returns Averages for a given Team"),
    path('addPlayerToTeam/', views.addPlayerToTeam, name="Add Player To a Team"),
    path('releasePlayer/', views.removePlayerFromTeam, name="Release Player"),
    path('availablePlayers/', views.getAvailablePlayers, name="Get Players Who Are Not On A Team"),
    path('teamPlayers/', views.getTeamPlayers, name="Get All Players on a Given Team"),

]
