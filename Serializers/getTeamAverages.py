from rest_framework import serializers


class criteriaAveragesList(object):
    def __init__(self, ids, names, averages):
        self.ids = ids
        self.names = names
        self.averages = averages


class teamAveragesSerializer(serializers.Serializer):
    ids = serializers.ListField()
    names = serializers.ListField()
    averages = serializers.ListField()