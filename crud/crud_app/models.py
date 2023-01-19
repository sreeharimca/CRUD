from django.db import models

# Create your models here.
# class Employee(models.Model):
#     eid=models.CharField(max_length=30)
#     ename=models.CharField(max_length=30)
#     eemail=models.EmailField()
#     econtact=models.CharField(max_length=20)
#
#
# class Details(models.Model):
#     name=models.CharField(max_length=30)
#     user=models.CharField(max_length=30)
#     phone=models.IntegerField()
#     password=models.CharField(max_length=30)



class regmodel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)

    phone=models.IntegerField()





class FileModel(models.Model):
    name=models.CharField(max_length=30)
    des=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.FileField(upload_to="crud_app/static")

