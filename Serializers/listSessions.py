from rest_framework import serializers


class sessionForList(object):
    def __init__(self, sessionIDs, sessionStarts):
        self.sessionIDs = sessionIDs
        self.sessionStarts = sessionStarts


class listSessionsSerializer(serializers.Serializer):
    sessionIDs = serializers.ListField()
    sessionStarts = serializers.ListField()