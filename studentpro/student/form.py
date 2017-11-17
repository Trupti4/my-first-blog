from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *

class StudentTableForm(forms.ModelForm):

    class Meta:
        model = StudentTable
        fields = ('student_ID', 'roll_no','student_name','division','student_class')

class ClassForm(forms.ModelForm):

	class Meta:
		model = Class
		fields = ('class_name',)

class DivisionForm(forms.ModelForm):

	class Meta:
		model = Division
		fields = ('division_name', 'stud_class')


