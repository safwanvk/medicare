# Serializers define the API representation.
from rest_framework import serializers, viewsets

from .models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']



