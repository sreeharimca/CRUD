

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os


# Create your views here.

#user form loading

# def load_form(request):
#     form=EmployeeForm
#     return render(request,'adduser.html',{'form':form})
#
# #click add button
#
# def add(request):
#     form =EmployeeForm(request.POST)
#     form.save()
#     return redirect(show)
#
# #show user
#
# def show(request):
#     employee=Employee.objects.all()
#     return render(request,'show_user.html',{'employee':employee})
#
#
# def edit(request,id):
#     employee=Employee.objects.get(id=id)
#     return render(request,'edit_user.html',{'employee':employee})
#
# def delete(request,id):
#     employee=Employee.objects.get(id=id)
#     employee.delete()
#     return redirect(show)
#
# def update(request,id):
#     employee=Employee.objects.get(id=id)
#     form=EmployeeForm(request.POST,instance=employee)
#     form.save()
#     return redirect(show)
#
#
# def bload(request):
#     form=DetailsForm()
#     return render(request,'bload_form.html',{'form':form})
#
# def badd(request):
#     form=DetailsForm(request.POST)
#     form.save()
#     return redirect(bshow)
#
# def bshow(request):
#     b=Details.objects.all()
#     return render(request,'bdisplay.html',{'b':b})
#
# def bdelete(request,id):
#     var=Details.objects.get(id=id)
#     var.delete()
#     return redirect(bshow)
#
# def bedit(request,id):
#     var=Details.objects.get(id=id)
#     return render(request,'bedit_user.html',{'var':var})
#
# def bupdate(request,id):
#     b=Details.objects.get(id=id)
#     form=DetailsForm(request.POST,instance=b)
#     form.save()
#     return redirect(bshow)

def a(request):
    return render(request,'index.html')



def register(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            nm= a.cleaned_data['name']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp= a.cleaned_data['cpassword']
            ph=a.cleaned_data['phone']

            if(ps==cp):
                b=regmodel(name=nm,email=em,password=ps,phone=ph)
                b.save()

                return redirect(login)
            else:
                return HttpResponse("failed")
        else:
            return HttpResponse("enter coorect values")
    else:
        return render(request,'registration.html')






def login(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']

            b=regmodel.objects.all()
            for i in b:
                if em==i.email and ps==i.password:
                     return  redirect(newindex)

            else:
                return HttpResponse("login failed2")

    else:
        return render(request,"login.html")


def newindex(request):
    return render(request,'intoindex.html')






def cload(request):
    a=FileForm()
    return render(request,'cload_form.html',{'a':a})

def cadd(request):
    b=FileForm(request.POST,request.FILES)
    b.save()
    return redirect(cshow)

def cshow(request):
    x=FileModel.objects.all()
    id=[]
    nm=[]
    dm=[]
    pm=[]
    im=[]
    for i in x:
        path=i.image
        im.append(str(path).split('/')[-1])
        nm.append(i.name)
        dm.append(i.des)
        pm.append(i.price)
        id.append(i.id)
    mylist=zip(id,nm,dm,pm,im)
    return render(request,'cdisplay.html',{'mylist':mylist})

def cedit(request,id):
    prod=FileModel.objects.get(id=id)
    li=str(prod.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(prod.image)>0:
                os.remove(prod.image.path)
            prod.image=request.FILES['image']
        prod.name=request.POST.get('name')
        prod.des=request.POST.get('des')
        prod.price = request.POST.get('price')
        prod.save()
        return redirect(cshow)
    context={'prod':prod ,'li':li}

    return render(request,'cedit.html',context)

def cdelete(request,id):
    prod=FileModel.objects.get(id=id)

    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(cshow)




