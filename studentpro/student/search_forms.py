from django.forms import ModelForm, Textarea, TextInput
from django import forms
from student.models import *



class StudentSearchForm(forms.Form):
   
    student_ID = forms.CharField(max_length=100, required=False)
    student_name = forms.ModelChoiceField(
        queryset= StudentTable.objects.all(),
       
        required=False
    )

    student_class =forms.ModelChoiceField(
        queryset= Class.objects.all(),required=False

    )

    student_division =forms.ModelChoiceField(
        queryset= Division.objects.all(),required=False

    )

   