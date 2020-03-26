from rest_framework import serializers


class criterionForList(object):
    def __init__(self, criteriaNames):
        self.criteriaNames = criteriaNames


class listCriteriaSerializer(serializers.Serializer):
    criteriaNames = serializers.ListField()