from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("pending","pending"),
        ("compleated","compleated"),
    )
    status=models.CharField(max_length=100,default="Pending",choices=options)


