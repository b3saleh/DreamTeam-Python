from rest_framework import serializers


class playerForList(object):
    def __init__(self, playerIDs, playerFirstNames, playerLastNames, playerTeams):
        self.playerIDs = playerIDs
        self.playerFirstNames = playerFirstNames
        self.playerLastNames = playerLastNames
        self.playerTeams = playerTeams


class listPlayersSerializer(serializers.Serializer):
    playerIDs = serializers.ListField()
    playerFirstNames = serializers.ListField()
    playerLastNames = serializers.ListField()
    playerTeams = serializers.ListField()