from rest_framework import serializers


class userInfo(object):
    def __init__(self, firstName, lastName, username, email):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email


class userInfoSerializer(serializers.Serializer):
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()