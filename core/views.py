from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer


# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

class CompanyViewSet(viewsets.ViewSet):
    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company Data Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Company Data"}
        return Response(dict_response)


company_list = CompanyViewSet.as_view({"get":"list"})
company_create = CompanyViewSet.as_view({"post":"create"})