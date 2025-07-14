from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from task.models import TodoTask
from django.contrib.auth.hashers import check_password
from datetime import datetime


def index(request):
        
    return render(request,"index.html")
# Create your views here.

def register(request):
    
    if request.method=="POST":
        INPusername=request.POST.get('username')
        INPemail=request.POST.get('email')
        INPpassword=request.POST.get('password')
        
        if(User.objects.filter(username=INPusername).exists()):
            messages.info(request,"Your Username was taken")
            return render(request,"register.html")
        elif(User.objects.filter(email=INPemail).exists()):
            messages.info(request,"Account with this email already exists")
            return render(request,"register.html")
        else:
            user=User.objects.create_user(username=INPusername, email=INPemail,password=INPpassword)
            user.save()
            todo=[]

            context={'user':user,'alltodo': todo}
            print(user.is_authenticated)
            return render(request,"home.html",context)
    return render(request,"register.html")

def login(request):
     
    if request.method=="POST":
      
        INPemail=request.POST.get('email')
        INPpassword=request.POST.get('password')
        user=User.objects.filter(email=INPemail).first()
       
        if(check_password(INPpassword,user.password)):
            print('password verified')
        else:
            # print()
            messages.info(request,"Your Login Information was incorrect")
            return render(request,"login.html")
        
    
        task=TodoTask.objects.filter(taskUser=user)
        context={'user':user, 'alltodo' : task}
        return render(request,"home.html", context)
    return render(request,"login.html")

def add(request):
    title=request.POST.get('title')
    desc=request.POST.get('desc')
    time=request.POST.get('time')
    date=request.POST.get('date')
    userid=request.POST.get('userid')
    user=User.objects.filter(id=userid).first()

    datetimeobj=datetime(int(date[0:4]),int(date[5:7]),int(date[8:10]),int(time[0:2]),int(time[3:5]),0)
    todo=TodoTask.objects.create(taskUser=user,taskTitle=title,taskDesc=desc,taksTime=datetimeobj,taskStat=False)
    todo.save()
    task=TodoTask.objects.filter(taskUser=user)
    context={'user':user, 'alltodo' : task}
    return render(request,'home.html',context)

def delete(request,taskID):
    todo=TodoTask.objects.filter(id=taskID).first()
    user=todo.taskUser
    todo.delete()
    task=TodoTask.objects.filter(taskUser=user)
    context={'user':user, 'alltodo' : task}
    return render(request,'home.html',context)
    

def incomplete(request,taskID):
    todo=TodoTask.objects.filter(id=taskID).first()
    user=todo.taskUser
    todo.taskStat=False
    todo.save()
    task=TodoTask.objects.filter(taskUser=user)
    context={'user':user, 'alltodo' : task}
    return render(request,'home.html',context)

def complete(request,taskID):
    todo=TodoTask.objects.filter(id=taskID).first()
    user=todo.taskUser
    todo.taskStat=True
    todo.save()
    task=TodoTask.objects.filter(taskUser=user)
    context={'user':user, 'alltodo' : task}
    return render(request,'home.html',context)

def update(request,taskID):
    
    todo=TodoTask.objects.filter(id=taskID).first()
    user=todo.taskUser
    if request.method=="POST":
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        todo.taskTitle=title
        todo.taskDesc=desc
        todo.save()
        task=TodoTask.objects.filter(taskUser=user)
        context={'user':user, 'alltodo' : task}
        return render(request,'home.html',context)
    context={'user':user, 'edit' : todo}
    return render(request,"update.html",context)

def logoutcall(request):
    logout(request)
    return redirect("index")