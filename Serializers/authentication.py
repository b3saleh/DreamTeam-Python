from rest_framework import serializers


class isValidUser(object):
    def __init__(self, isValid):
        self.isValid = isValid


class authenticationSerializer(serializers.Serializer):
    isValid = serializers.BooleanField()