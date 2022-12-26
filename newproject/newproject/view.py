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
    name = "1";
    #  query = "select * from tbl1 where name='" + name + "'";
    query = "select email from contact where id="+'"{}"'.format(name)
    #query = "select email from tbl1 where name=%s", [name]
    #print('query', query)
    cursor.execute(query)
    result = cursor.fetchall()
    print("result", result)

    return render(request, 'newproject/contact.html')


def profile(request):
    return render(request, 'newproject/profile.html')
