from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm,UserLoginForm,TodoForm,TodoUpdateForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from todoApp.models import TodoModel

# Create your views here.
class UserRegisterView(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,'user_register.html',{'form':form})
    
    def post(self,request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Registration Successful")
            return redirect('user_login')
        else:
            messages.warning(request,"user already exist")
            return redirect('user_register')
        
class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'user_login.html',{'form':form})
    
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(request,"Login Successful")
            return redirect('home_view')
        
        else:
            messages.warning(request,"Invalid User")
            return redirect("user_login")
        


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("user_login")
        
class Home(View):
    def get(self,request):
        if request.user.is_authenticated:
            todos=TodoModel.objects.filter(user=request.user)
            print(todos)
            return render(request,'home.html',{'todos':todos})
        else:
            messages.warning(request,"You must login first")
            return redirect("user_login")
    



class TodoCraeteView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,'todo_create.html',{'form':form})
    
    def post(self,request):
        form=TodoForm(request.POST)
        user=request.user
        if form.is_valid():
            print(form.cleaned_data)
            TodoModel.objects.create(**form.cleaned_data,user=user)
            return redirect("home_view")
        

class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        todo=TodoModel.objects.get(id=kwargs.get("id"))
        todo.delete()
        messages.success(request,"todo deleted!")
        return redirect('home_view')
    
class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        todo=TodoModel.objects.get(id=kwargs.get("id"))
        form=TodoUpdateForm(instance=todo)
        return render(request,"todo_update.html",{'form':form})
    def post(self,request,*args,**kwargs):
        todo=TodoModel.objects.get(id=kwargs.get("id"))
        title=request.POST.get("title")
        content=request.POST.get("content")
        status=request.POST.get("status")
        todo.title=title
        todo.content=content
        todo.status=status
        todo.save()
        messages.success(request,"Todo Updated!")
        return redirect("home_view")



    
    
    


