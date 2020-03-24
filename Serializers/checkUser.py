from rest_framework import serializers


class userID(object):
    def __init__(self, userID):
        self.userID = userID


class userIDSerializer(serializers.Serializer):
    userID = serializers.IntegerField()