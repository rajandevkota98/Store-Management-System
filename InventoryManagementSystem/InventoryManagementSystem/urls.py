"""InventoryManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from stockmanagement import views
router= routers.DefaultRouter()

from stockmanagement.views import CompanyNameViewSet, EmployeebankByidViewSet, EmployeesalaryByidViewSet, \
    InventoryNameViewSet
from stockmanagement.views import  CompanyonlyViewSet
from stockmanagement.views import InventoryViewSet
from  stockmanagement.views import  CompanyAccountViewSet
from stockmanagement.views import EmployeeViewSet
from  stockmanagement.views import EmployeeSalaryViewSet
from  stockmanagement.views import EmployeeBankViewSet
from stockmanagement.views import BillgenerateViewSet
from stockmanagement.views import HomeViewSet
from  stockmanagement.views import RequestViewset

router.register("company",views.CompanyViewSet, basename= "company")
router.register("companybank",views.CompanyBankViewSet, basename= "companybank")
router.register("inventory",views.InventoryViewSet, basename= "inventory")
router.register("companyaccount",views.CompanyAccountViewSet, basename= "companyaccount")
router.register("employee",views.EmployeeViewSet, basename= "employee")
router.register("employeebank",views.EmployeeBankViewSet, basename= "employeebank")
router.register("employeesalary",views.EmployeeSalaryViewSet, basename= "employeesalary")
router.register("billgenerate",views.BillgenerateViewSet, basename= "billgenerate")
router.register("request",views.RequestViewset, basename= "request")
router.register("homeAPI",views.HomeViewSet, basename= "homeAPI")








from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',  include(router.urls)),
    path('api/gettoken/',  TokenObtainPairView.as_view(), name = "gettoken"),
    path('api/refresh_token/',TokenRefreshView.as_view(), name= "refresh_token"),
    path('api/companybyname/<str:name>',CompanyNameViewSet.as_view(), name= "companybyname"),
    path('api/companyonly/',CompanyonlyViewSet.as_view(), name= "companyonly"),
    path('api/employeebankbyid/<str:employee_id>', EmployeebankByidViewSet.as_view(), name="employeebankbyid"),
    path('api/employeesalarybyid/<str:employee_id>', EmployeesalaryByidViewSet.as_view(), name="employeesalarybyid"),
    path('api/inventorybyname/<str:name>', InventoryNameViewSet.as_view(), name="companybyname"),

]
