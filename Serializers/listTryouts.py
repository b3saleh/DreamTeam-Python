from rest_framework import serializers


class tryoutForList(object):
    def __init__(self, tryoutIDs, tryoutNames):
        self.tryoutIDs = tryoutIDs
        self.tryoutNames = tryoutNames


class listTryoutsSerializer(serializers.Serializer):
    tryoutIDs = serializers.ListField()
    tryoutNames = serializers.ListField()