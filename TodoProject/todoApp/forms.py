from django import forms
from django.contrib.auth.models import User
from todoApp.models import TodoModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username',"first_name","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }


class TodoForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        fields=['title','content']
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        fields=['title','content','status']
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
            "status":forms.Select(attrs={"class":"form-control"}),
        }

