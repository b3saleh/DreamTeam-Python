from rest_framework import serializers


class commentForList(object):
    def __init__(self, commentIDs, comments, commenters, commentTimes):
        self.commentIDs = commentIDs
        self.comments = comments
        self.commenters = commenters
        self.commentTimes = commentTimes


class listCommentsSerializer(serializers.Serializer):
    commentIDs = serializers.ListField()
    comments = serializers.ListField()
    commenters = serializers.ListField()
    commentTimes = serializers.ListField()