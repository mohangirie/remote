from django.shortcuts import render
from .forms import Employee_Form
from .models import Employee

# Create your views here.
def employee_view(request):
    if request.method=="POST":
        eform= Employee_Form(request.POST)

        empno1= request.POST.get('empno','')
        firstname1= request.POST.get('firstname','')
        lastname1=request.POST.get('lastname','')
        salary1=request.POST.get('salary','')
        location1=request.POST.get('location','')
        company1=request.POST.get('company','')
        position1=request.POST.get('position','')
        mobile1=request.POST.get('mobile','')
        email1=request.POST.get('email','')
        data=Employee(
            empno=empno1,
            firstname=firstname1,
            lastname=lastname1,
            salary=salary1,
            location=location1,
            company=company1,
            position=position1,
            mobile=mobile1,
            email=email1,
        )
        data.save()

        return render(request,'employee.html',{'eform':eform})
    else:
        eform=Employee_Form()
        return render(request,'employee.html',{'eform':eform})

def Employee_details(request):
    edata=Employee.objects.all()
    return render(request,'EmployeeDetails.html',{'edata':edata})
    return render(request,'EmployeeDetails.html',{'edata':edata})

def home(request):
    return render(request,"home.html")
