from rest_framework import serializers


class playerForList(object):
    def __init__(self, playerIDs, playerFirstNames, playerLastNames):
        self.playerIDs = playerIDs
        self.playerFirstNames = playerFirstNames
        self.playerLastNames = playerLastNames


class listPlayersSerializer(serializers.Serializer):
    playerIDs = serializers.ListField()
    playerFirstNames = serializers.ListField()
    playerLastNames = serializers.ListField()