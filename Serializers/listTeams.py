from rest_framework import serializers


class listOfTeams(object):
    def __init__(self, teamIDs, teamNames):
        self.teamIDs = teamIDs
        self.teamNames = teamNames


class teamListSerializer(serializers.Serializer):
    teamIDs = serializers.ListField()
    teamNames = serializers.ListField()