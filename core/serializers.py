# Serializers define the API representation.
from rest_framework import serializers, viewsets

from .models import Company, CompanyBank


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = '__all__'
