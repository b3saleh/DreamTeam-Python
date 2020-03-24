from rest_framework import serializers


class criterionForList(object):
    def __init__(self, criterionName):
        self.criterionName = criterionName


class listCriteriaSerializer(serializers.Serializer):
    criterionName = serializers.CharField()