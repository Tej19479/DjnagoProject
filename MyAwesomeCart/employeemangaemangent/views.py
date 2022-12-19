import json
from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Role, Department, Employee
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'employeemangaemangent/index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps

    }
    print(context)
    return render(request, 'employeemangaemangent/all_employee.html', context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        salary = int(request.POST["salary"])
        bonus = request.POST["bonus"]

        phone = int(request.POST["phone"])
        dept = int(request.POST["dept"])
        dept = int(request.POST["dept"])
        role = int(request.POST["role"])
        print("fffffffff", bonus)
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, phone=phone, dept_id=dept,
                           role_id=role, bonus=bonus, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Pass")

    elif request.method == "Get":
        return HttpResponse("GEt")

    return render(request, 'employeemangaemangent/add_employee.html')


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            print("emp_id remove", emp_id)

            emp_to_be_removed = Employee.objects.get(id=emp_id)
            print("Fecting the ata", emp_to_be_removed)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please enter A vaild EMP ID")

    emps = Employee.objects.all()
    context = {
        'emps': emps

    }
    print(context)
    return render(request, 'employeemangaemangent/remove_employee.html', context)


def filter_emp(request):
    if request.method == "POST":
        name = request.POST["name"]
        dept = request.POST["dept"]
        role = request.POST["role"]
        print("sorting parameter value=======", name, dept, role)

        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context = {
            'emps': emps
        }
        return render(request, 'employeemangaemangent/all_employee.html', context)
    elif request.method=="GET":
        return render(request, 'employeemangaemangent/filter_employee.html')
    else:
        return HttpResponse("AN occureed")
