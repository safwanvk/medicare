"""msms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from core.views import CompanyViewSet, CompanyBankViewSet, CompanyNameViewSet, MedicineViewSet, CompanyOnlyViewSet,\
    CompanyAccountViewset, EmployeeViewset, EmployeeBankViewset, EmployeeSalaryViewset, EmployeeBankByEIDViewSet, \
    EmployeeSalaryByEIDViewSet, MedicineByNameViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'company_bank', CompanyBankViewSet, basename='company_bank')
router.register(r'medicine', MedicineViewSet, basename='medicine')
router.register("company_account", CompanyAccountViewset, basename="company_account")
router.register("employee", EmployeeViewset, basename="employee")
router.register("employee_all_bank", EmployeeBankViewset, basename="employee_all_bank")
router.register("employee_all_salary", EmployeeSalaryViewset, basename="employee_all_salary")

import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/refresh_token/', TokenRefreshView.as_view(), name="refresh_token"),
    path('api/company_by_name/<str:name>', CompanyNameViewSet.as_view(), name="company_by_name"),
    path('api/medicine_by_name/<str:name>', MedicineByNameViewSet.as_view(), name="medicine_by_name"),
    path('api/company_only/', CompanyOnlyViewSet.as_view(), name="company_only"),
    path('api/employee_bank_by_id/<str:employee_id>', EmployeeBankByEIDViewSet.as_view(), name="employee_bank_by_id"),
    path('api/employee_salary_by_id/<str:employee_id>', EmployeeSalaryByEIDViewSet.as_view(), name="employee_salary_by_id"),
]
