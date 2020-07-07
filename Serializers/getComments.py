from rest_framework import serializers


class commentForList(object):
    def __init__(self, commentIDs, comments, commenterFirstNames, commenterLastNames, commenterIDs, commentTimes):
        self.commentIDs = commentIDs
        self.comments = comments
        self.commenterFirstNames = commenterFirstNames
        self.commenterLastNames = commenterLastNames
        self.commenterIDs = commenterIDs
        self.commentTimes = commentTimes

class listCommentsSerializer(serializers.Serializer):
    commentIDs = serializers.ListField()
    comments = serializers.ListField()
    commenterFirstNames = serializers.ListField()
    commenterLastNames = serializers.ListField()
    commenterIDs = serializers.ListField()
    commentTimes = serializers.ListField()