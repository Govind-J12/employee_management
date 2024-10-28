from django.shortcuts import render,redirect
from . models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def add_employee(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        role = request.POST.get("role") 
        date_joined = request.POST.get("date_joined") 
        data = addemployee(name=name,email=email,department=department,role=role,date_joined=date_joined)
        data.save()
    return render(request,'add_employee.html')

def view_all_employee(request):
    data=addemployee.objects.all()
    return render(request,'list_all_employee.html',{'res':data})

def emp_delete(request,id):
    data=addemployee.objects.get(pk=id)
    data.delete()
    return redirect(view_all_employee)

def emp_update(request,id):
    data=addemployee.objects.get(pk=id)
    return render(request,'update_emp.html',{'res':data})


def emp_updates(request,id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        role = request.POST.get("role") 
        date_joined = request.POST.get("date_joined") 
        data = addemployee(name=name,email=email,department=department,role=role,date_joined=date_joined,id=id)
        data.save()
        return redirect(view_all_employee)
    return render(request,'update_emp.html')



    


