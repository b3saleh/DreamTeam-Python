from rest_framework import serializers


class tryoutForList(object):
    def __init__(self, tryoutID, tryoutName):
        self.tryoutID = tryoutID
        self.tryoutName = tryoutName


class listTryoutsSerializer(serializers.Serializer):
    tryoutID = serializers.CharField()
    tryoutName = serializers.CharField()