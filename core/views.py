from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime, timedelta

from .models import Company, CompanyBank, Medicine, MedicalDetails, CompanyAccount, Employee, EmployeeBank, \
    EmployeeSalary, CustomerRequest, Bill, BillDetails
from .serializers import CompanySerializer, CompanyBankSerializer, MedicineSerializer, MedicalDetailsSerializer, \
    MedicalDetailsSerializerSimple, CompanyAccountSerializer, EmployeeSerializer, EmployeeBankSerializer, \
    EmployeeSalarySerializer, CustomerSerializer, BillSerializer, BillDetailsSerializer, CustomerRequestSerializer


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


class MedicineByNameViewSet(generics.ListAPIView):
    serializer_class = MedicineSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Medicine.objects.filter(name__contains=name)


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


# Employee Salary Viewset
class EmployeeSalaryViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = EmployeeSalarySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Employee Salary Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Employee Salary"}
        return Response(dict_response)

    def list(self, request):
        employee_salary = EmployeeSalary.objects.all()
        serializer = EmployeeSalarySerializer(employee_salary, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Employee Salary List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = EmployeeSalary.objects.all()
        employee_salary = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSalarySerializer(employee_salary, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = EmployeeSalary.objects.all()
        employee_salary = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSalarySerializer(employee_salary, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data Has Been Updated"})


class EmployeeBankByEIDViewSet(generics.ListAPIView):
    serializer_class = EmployeeBankSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.kwargs["employee_id"]
        return EmployeeBank.objects.filter(employee_id=employee_id)


class EmployeeSalaryByEIDViewSet(generics.ListAPIView):
    serializer_class = EmployeeSalarySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.kwargs["employee_id"]
        return EmployeeSalary.objects.filter(employee_id=employee_id)

class GenerateBillViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        #try:
            #First #Save Customer Data
        serializer = CustomerSerializer(data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()

        customer_id = serializer.data['id']

        #Save Bill Data
        billdata={}
        billdata["customer_id"]=customer_id

        serializer2 = BillSerializer(data=billdata, context={"request": request})
        serializer2.is_valid()
        serializer2.save()
        bill_id = serializer2.data['id']

        # Adding and Saving Id into Medicine Details Table
        medicine_details_list = []
        for medicine_detail in request.data["medicine_details"]:
            print(medicine_detail)
            medicine_detail1={}
            medicine_detail1["medicine_id"] = medicine_detail["id"]
            medicine_detail1["bill_id"] = bill_id
            medicine_detail1["qty"] = medicine_detail["qty"]

            medicine_deduct=Medicine.objects.get(id=medicine_detail["id"])
            medicine_deduct.in_stock_total=int(medicine_deduct.in_stock_total)-int(medicine_detail['qty'])
            medicine_deduct.save()

            medicine_details_list.append(medicine_detail1)
            #print(medicine_detail)

        serializer3 = BillDetailsSerializer(data=medicine_details_list, many=True,
                                               context={"request": request})
        serializer3.is_valid()
        serializer3.save()

        dict_response = {"error": False, "message": "Bill Generate Successfully"}
        #except:
            #dict_response = {"error": True, "message": "Error During Generating BIll"}
        return Response(dict_response)


class CustomerRequestViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        customer_request=CustomerRequest.objects.all()
        serializer=CustomerRequestSerializer(customer_request,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Customer Request Data","data":serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer=CustomerRequestSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Customer Request Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Customer Request Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = CustomerRequest.objects.all()
        customer_request = get_object_or_404(queryset, pk=pk)
        serializer = CustomerRequestSerializer(customer_request, context={"request": request})

        serializer_data = serializer.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=CustomerRequest.objects.all()
            customer_request=get_object_or_404(queryset,pk=pk)
            serializer=CustomerRequestSerializer(customer_request,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Customer Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Customer Data"}

        return Response(dict_response)

class HomeApiViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        customer_request=CustomerRequest.objects.all()
        customer_request_serializer=CustomerRequestSerializer(customer_request,many=True,context={"request":request})


        bill_count=Bill.objects.all()
        bill_count_serializer=BillSerializer(bill_count,many=True,context={"request":request})

        medicine_count=Medicine.objects.all()
        medicine_count_serializer=MedicineSerializer(medicine_count,many=True,context={"request":request})

        company_count=Company.objects.all()
        company_count_serializer=CompanySerializer(company_count,many=True,context={"request":request})

        employee_count=Employee.objects.all()
        employee_count_serializer=EmployeeSerializer(employee_count,many=True,context={"request":request})

        bill_details=BillDetails.objects.all()
        profit_amt=0
        sell_amt=0
        buy_amt=0
        for bill in bill_details:
            buy_amt=float(buy_amt+float(bill.medicine_id.buy_price))*int(bill.qty)
            sell_amt=float(sell_amt+float(bill.medicine_id.sell_price))*int(bill.qty)

        profit_amt=sell_amt-buy_amt


        customer_request_pending=CustomerRequest.objects.filter(status=False)
        customer_request_pending_serializer=CustomerRequestSerializer(customer_request_pending,many=True,context={"request":request})

        customer_request_completed=CustomerRequest.objects.filter(status=True)
        customer_request_completed_serializer=CustomerRequestSerializer(customer_request_completed,many=True,context={"request":request})

        current_date=datetime.today().strftime("%Y-%m-%d")
        current_date1=datetime.today()
        current_date_7days=current_date1+timedelta(days=7)
        current_date_7days=current_date_7days.strftime("%Y-%m-%d")
        bill_details_today=BillDetails.objects.filter(added_on__date=current_date)
        profit_amt_today=0
        sell_amt_today=0
        buy_amt_today=0
        for bill in bill_details_today:
            buy_amt_today=float(buy_amt_today+float(bill.medicine_id.buy_price))*int(bill.qty)
            sell_amt_today=float(sell_amt_today+float(bill.medicine_id.sell_price))*int(bill.qty)


        profit_amt_today=sell_amt_today-buy_amt_today


        medicine_expire=Medicine.objects.filter(expire_date__range=[current_date,current_date_7days])
        medicine_expire_serializer=MedicineSerializer(medicine_expire,many=True,context={"request":request})

        bill_dates=BillDetails.objects.order_by().values("added_on__date").distinct()
        profit_chart_list=[]
        sell_chart_list=[]
        buy_chart_list=[]
        for billdate in bill_dates:
            access_date=billdate["added_on__date"]

            bill_data=BillDetails.objects.filter(added_on__date=access_date)
            profit_amt_inner=0
            sell_amt_inner=0
            buy_amt_inner=0

            for billsingle in bill_data:
                buy_amt_inner = float(buy_amt_inner + float(billsingle.medicine_id.buy_price)) * int(billsingle.qty)
                sell_amt_inner = float(sell_amt_inner + float(billsingle.medicine_id.sell_price)) * int(billsingle.qty)

            profit_amt_inner = sell_amt_inner - buy_amt_inner

            profit_chart_list.append({"date":access_date,"amt":profit_amt_inner})
            sell_chart_list.append({"date":access_date,"amt":sell_amt_inner})
            buy_chart_list.append({"date":access_date,"amt":buy_amt_inner})

        dict_respone={"error":False,"message":"Home Page Data","customer_request":len(customer_request_serializer.data),"bill_count":len(bill_count_serializer.data),"medicine_count":len(medicine_count_serializer.data),"company_count":len(company_count_serializer.data),"employee_count":len(employee_count_serializer.data),"sell_total":sell_amt,"buy_total":buy_amt,"profit_total":profit_amt,"request_pending":len(customer_request_pending_serializer.data),"request_completed":len(customer_request_completed_serializer.data),"profit_amt_today":profit_amt_today,"sell_amt_today":sell_amt_today,"medicine_expire_serializer_data":len(medicine_expire_serializer.data),"sell_chart":sell_chart_list,"buy_chart":buy_chart_list,"profit_chart":profit_chart_list}
        return  Response(dict_respone)


company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
