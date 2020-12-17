from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Company, CompanyBank, Medicine, MedicalDetails, CompanyAccount, Employee, EmployeeBank
from .serializers import CompanySerializer, CompanyBankSerializer, MedicineSerializer, MedicalDetailsSerializer, \
    MedicalDetailsSerializerSimple, CompanyAccountSerializer, EmployeeSerializer, EmployeeBankSerializer


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


class CompanyOnlyViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()


class MedicineViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
        queryset = Medicine.objects.all()
        medicine = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializer(medicine, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        # print(request.data["medicine_details"])
        for salt_detail in request.data["medicine_details"]:
            if salt_detail["id"] == 0:
                # For Insert New Salt Details
                del salt_detail["id"]
                salt_detail["medicine_id"] = serializer.data["id"]
                serializer2 = MedicalDetailsSerializer(data=salt_detail, context={"request": request})
                serializer2.is_valid()
                serializer2.save()
            else:
                # For Update Salt Details
                queryset2 = MedicalDetails.objects.all()
                medicine_salt = get_object_or_404(queryset2, pk=salt_detail["id"])
                del salt_detail["id"]
                serializer3 = MedicalDetailsSerializer(medicine_salt, data=salt_detail, context={"request": request})
                serializer3.is_valid()
                serializer3.save()
                print("UPDATE")

        return Response({"error": False, "message": "Data Has Been Updated"})


# Company Account Viewset
class CompanyAccountViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CompanyAccountSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company Account Data Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Company Account Data"}
        return Response(dict_response)

    def list(self, request):
        company_account = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializer(company_account, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company Account List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = CompanyAccount.objects.all()
        company_account = get_object_or_404(queryset, pk=pk)
        serializer = CompanyAccountSerializer(company_account, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = CompanyAccount.objects.all()
        company_account = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializer(company_account, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data Has Been Updated"})


# Employee Viewset
class EmployeeViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Employee Data Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Employee Data"}
        return Response(dict_response)

    def list(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Employee List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(employee, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data Has Been Updated"})


# Employee Bank Viewset
class EmployeeBankViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = EmployeeBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Employee Bank Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Employee Bank"}
        return Response(dict_response)

    def list(self, request):
        employee_bank = EmployeeBank.objects.all()
        serializer = EmployeeBankSerializer(employee_bank, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Employee Bank List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = EmployeeBank.objects.all()
        employee_bank = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeBankSerializer(employee_bank, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = EmployeeBank.objects.all()
        employee_bank = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeBankSerializer(employee_bank, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data Has Been Updated"})


company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
