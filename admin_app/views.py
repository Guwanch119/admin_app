from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def employee(request):
    return render(request,'employee.html')

def add_user(request):
    return render (request,'add_user.html')

def employee_profile(request):
    return render (request,'employee_profile.html')

def edit_employee(request):
    return render (request,'edit_employee.html')

def works(request):
    return render (request,'works.html')
