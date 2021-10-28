from django.shortcuts import render
from .forms import EmpForm
from .models import Employe
# Create your views here.
def add(request):
    empForm=EmpForm()
    return render(request,'add.html',{'empForm':empForm})

def insertEmp(request):
    if request.method=="POST":
        empForm = EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return render(request,'getEmpDetails.html')
        else:
            return render(request,'add.htnl')
    else:
        return render(request,'add.html')

def show(request):
    employees = Employe.objects.all()
    return render(request,'show.html',{'employees':employees})

def editEmp(request,eid):
    emp = Employe.objects.get(eid=eid)
    return render(request,'edit.html',{'emp':emp})


def updateEmp(request,eid):
    if request.method == "POST":
        emp = Employe.objects.get(eid=eid)
        form = EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return render(request,'show.html')
        else:
            return render(request,'edit.html',{'emp':emp,'msg':'Details Not Updated...!!!'})
    else:
            return render(request,'edit.html',{'emp':emp,'msg':'Details Not Updated...!!!'})

def deleteEmp(request,eid):
    emp = Employe.objects.get(eid=eid)
    emp.delete()
    return render(request,'show.html')
