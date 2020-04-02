from rest_framework import serializers


class playerInfo(object):
    def __init__(self, thisPlayer):
        self.firstName = thisPlayer.firstName
        self.lastName = thisPlayer.lastName
        self.email = thisPlayer.email
        self.teamID = thisPlayer.teamID


class playerInfoSerializer(serializers.Serializer):
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    email = serializers.CharField()
    teamID = serializers.IntegerField()