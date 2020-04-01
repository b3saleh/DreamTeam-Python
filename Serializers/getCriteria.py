from rest_framework import serializers


class gradesForList(object):
    def __init__(self, criteriaGrades, criteriaIDs):
        self.criteriaGrades = criteriaGrades
        self.criteriaIDs = criteriaIDs


class listGradesSerializer(serializers.Serializer):
    criteriaGrades = serializers.ListField()
    criteriaIDs = serializers.ListField()