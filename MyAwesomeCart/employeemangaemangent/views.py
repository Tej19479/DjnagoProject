import json
from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Role, Department, Employee
from datetime import datetime
from django.db.models import Q
import math


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
    elif request.method == "GET":
        return render(request, 'employeemangaemangent/filter_employee.html')
    else:
        return HttpResponse("AN occureed")


def amzotionchart(request):
    ''' print("Enter an amount to borrow")
    p = input()
    print("Enter an annual interest rate as a decimal value")
    r = input()
    print("Enter a loan lenght in years")
    t = input()

    p = float(p)
    r = float(r)
    t = float(t)'''
    p = 10000
    r = 5
    t = 3
    r = (r / 100) / 12

    # m = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)

    m = (p * (r / 12) * (math.pow(1 + r / 12, 12 * t))) / (math.pow(1 + r / 12, 12 + t) - 1)
    print("Your payment will be: Rupiya" + str(m))
    print("Month\tStartingBalance\tInterestRate\tInterestCharge\tPayment\tEndingBalance")

    month = 12 * t
    month = int(month)
    startingBalance = p
    endingBalance = p
    months = []
    print("months", months)
    for i in range(1, month + 1):
        interestCharge = r / 12 * startingBalance
        endingBalance = startingBalance + interestCharge - m
        months.append(
            [i, "₹ " + str(round(startingBalance, 2)), "₹ " + str(round(interestCharge, 2)), "₹ " + str(round(m, 2)),
             "₹ " + str(round(endingBalance, 2))])

        '''print(
            str(i) + "\t\t$" + str(round(startingBalance, 2)) + "\t\t$" + str(round(interestCharge, 2)) + "\t\t$" + str(
                round(m, 2)) + "\t\t$" + str(round(endingBalance, 2)))'''
        ''' months=i
        startingBalances=str(round(startingBalance, 2))
        interestscharges=str(round(interestCharge, 2))
        emimothnly=str(round(m, 2))
        endingbalances=str(round(endingBalance, 2))'''
        startingBalance = endingBalance
    print(months)
    context = {'months': months}
    return render(request, 'employeemangaemangent/emi.html', context)
