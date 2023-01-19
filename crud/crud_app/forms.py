from django import forms
from .models import *

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model=Employee
#         fields="__all__"
#
#
# class DetailsForm(forms.ModelForm):
#     class Meta:
#         model=Details
#         fields="__all__"

class regform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=30)
    cpassword=forms.CharField(max_length=30)

    phone = forms.IntegerField()


class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=30)




class FileForm(forms.ModelForm):
    class Meta:
        model=FileModel
        fields="__all__"