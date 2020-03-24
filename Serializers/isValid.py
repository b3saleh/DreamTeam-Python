from rest_framework import serializers


class isValid(object):
    def __init__(self, is_valid):
        self.is_valid = is_valid


class isValidSerializer(serializers.Serializer):
    is_valid = serializers.BooleanField()