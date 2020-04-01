from rest_framework import serializers


class criterionForList(object):
    def __init__(self, criteriaNames, criteriaIDs):
        self.criteriaNames = criteriaNames
        self.criteriaIDs = criteriaIDs


class listCriteriaSerializer(serializers.Serializer):
    criteriaNames = serializers.ListField()
    criteriaIDs = serializers.ListField()