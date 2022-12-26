from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="project1"
)
cursor = mydb.cursor()


# cursor.execute('SHOW TABLES')


def home(request):
    return render(request, 'newproject/home.html')


def contact(request):
    query = 'select * from tbl1'
    cursor.execute(query)

    for x in cursor:
        print(x)

    return render(request, 'newproject/contact.html')


def profile(request):
    return render(request, 'newproject/profile.html')
