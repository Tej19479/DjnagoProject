from django.urls import path
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="employeemangaemangent"),
    path('/all_emp', views.all_emp, name="all_emp"),
    path('/add_emp', views.add_emp, name="add_emp"),
    path('/remove_emp/', views.remove_emp, name="remove_emp"),
    path('/remove_emp/', views.remove_emp, name="remove_emp"),
    path('/remove_emp/<int:emp_id>', views.remove_emp, name="remove_emp"),

    path('/filter_emp', views.filter_emp, name="filter_emp"),
    path('/amzotionchart', views.amzotionchart, name="amzotionchart")

]
