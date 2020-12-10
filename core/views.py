from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Company, CompanyBank, Medicine, MedicalDetails
from .serializers import CompanySerializer, CompanyBankSerializer, MedicineSerializer, MedicalDetailsSerializer, \
    MedicalDetailsSerializerSimple


# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Company Details of Current Company ID
        company_bank_details = CompanyBank.objects.filter(company_id=serializer_data["id"])
        company_bank_details_serializers = CompanyBankSerializer(company_bank_details, many=True)
        serializer_data["company_bank"] = company_bank_details_serializers.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Successfully Updated Company Data"}
        except:
            dict_response = {"error": True, "message": "Error During Updating Company Data"}

        return Response(dict_response)


class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CompanyBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company Bank Data Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Company Data"}
        return Response(dict_response)

    def list(self, request):
        company_bank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(company_bank, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company Bank List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        company_bank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializer(company_bank, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            company_bank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(company_bank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Successfully Updated Company Bank Data"}
        except:
            dict_response = {"error": True, "message": "Error During Updating Company Bank Data"}

        return Response(dict_response)


class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Company.objects.filter(name=name)


class MedicineViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        def create(self, request):
            try:
                serializer = MedicineSerializer(data=request.data, context={"request": request})
                serializer.is_valid(raise_exception=True)
                serializer.save()

                medicine_id = serializer.data['id']
                # Access The Serializer Id Which JUSt SAVE in OUR DATABASE TABLE
                # print(medicine_id)

                # Adding and Saving Id into Medicine Details Table
                medicine_details_list = []
                for medicine_detail in request.data["medicine_details"]:
                    print(medicine_detail)
                    # Adding medicine id which will work for medicine details serializer
                    medicine_detail["medicine_id"] = medicine_id
                    medicine_details_list.append(medicine_detail)
                    print(medicine_detail)

                serializer2 = MedicalDetailsSerializer(data=medicine_details_list, many=True,
                                                       context={"request": request})
                serializer2.is_valid()
                serializer2.save()

                dict_response = {"error": False, "message": "Medicine Data Save Successfully"}
            except:
                dict_response = {"error": True, "message": "Error During Saving Medicine Data"}
            return Response(dict_response)

    def list(self, request):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(medicine, many=True, context={"request": request})

        medicine_data = serializer.data
        new_medicine_list = []

        # Adding Extra Key for Medicine Details in Medicine
        for medicine in medicine_data:
            # Accessing All the Medicine Details of Current Medicine ID
            medicine_details = MedicalDetails.objects.filter(medicine_id=medicine["id"])
            medicine_details_serializers = MedicalDetailsSerializerSimple(medicine_details, many=True)
            medicine["medicine_details"] = medicine_details_serializers.data
            new_medicine_list.append(medicine)

        response_dict = {"error": False, "message": "All Medicine List Data", "data": new_medicine_list}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Medicine.objects.all()
        medicine = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializer(medicine, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID
        medicine_details = MedicalDetails.objects.filter(medicine_id=serializer_data["id"])
        medicine_details_serializers = MedicalDetailsSerializerSimple(medicine_details, many=True)
        serializer_data["medicine_details"] = medicine_details_serializers.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            medicine = get_object_or_404(queryset, pk=pk)
            serializer = MedicineSerializer(medicine, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Successfully Updated Medicine Data"}
        except:
            dict_response = {"error": True, "message": "Error During Updating Medicine Data"}

        return Response(dict_response)


company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
