from django.shortcuts import render redirect
from django.contrib.auth.models import User
from django.contrib.auth.import authenticate,login,logout
from.models import Student

def home(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,'index.html',{"data":data})
def insertData(request):
    if request.method=='POST'











def updateData(request, id):
    if request.method =='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender



        edit = Student.objects.get(id=id)
        edit.name =









        d=Student.objects.get(id=id)
        d.delete()
        return redirect('/')
        # return renderf(request,'index.html)