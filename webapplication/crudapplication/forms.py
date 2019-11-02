from django import forms
from crudapplication.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__" # This denotes that we need all fields of the model
