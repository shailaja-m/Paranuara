from django.urls import path

from . import views

urlpatterns = [
    path('company/<str:name>/', views.findAllEmployeesInCompany, name='findAllEmployeesInCompany'),
    path('friends', views.findCommonFriends, name='findCommonFriends'),
    path('employeeinformation/<str:name>/', views.findEmployee, name='findEmployee'),
]
