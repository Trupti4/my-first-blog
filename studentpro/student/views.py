from django.shortcuts import render

from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView
from student.models import *
from student.form import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from student.search_forms import *




# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'student/home.html'



class StudentTableListView(ListView):
    template_name = 'student/student.html'
    model = StudentTable


    form_class = StudentTable

    def get_context_data(self, **kwargs):
        context = super(StudentTableListView, self).get_context_data(**kwargs)
        if self.request.GET:
            context['form'] = StudentSearchForm(self.request.GET)
        else:
            context['form'] = StudentSearchForm()

        return context

    def get_queryset(self):
        args = {}
        student_name = self.request.GET.get('student_name', False)
        student_ID = self.request.GET.get('student_ID', False)
        student_class =self.request.GET.get('student_class', False)
        student_division=self.request.GET.get('student_division', False)
        
        if student_ID:
            args['student_ID'] = student_ID

        if student_class:
            args['student_class'] = student_class

        if student_division:
            args['division'] = student_division

        if student_name:
            args['student_ID'] = student_name

        return StudentTable.objects.filter(**args)

   


class StudentTableCreate(CreateView):
    model = StudentTable
    form_class = StudentTableForm
    


    def get_success_url(self):
        return reverse('student')

    def form_valid(self, form):
        student_ID = form.save()
        messages.success(self.request, 'Student Details Added Successfully')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ))

class StudentTableUpdate(UpdateView):
    model = StudentTable
    form_class = StudentTableForm
    


    def get_success_url(self):
        return reverse('student')

    def form_valid(self, form):
        student_ID = form.save()
        messages.success(self.request, 'Student Details Added Successfully')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ))

class StudentTableDetail(DetailView):
	model = StudentTable 



class ClassListView(ListView):
    template_name = 'student/student_class.html'
    model = Class

class ClassCreate(CreateView):
    model = Class
    form_class = ClassForm

    def get_success_url(self):
        return reverse('student_class')

    def form_valid(self, form):
        id = form.save()
        messages.success(self.request, 'Student Class Added Successfully')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ))
    
class ClassUpdate(UpdateView):
    model = Class
    form_class = ClassForm
    


    def get_success_url(self):
        return reverse('student_class')

    def form_valid(self, form):
        id = form.save()
        messages.success(self.request, 'Student Class Added Successfully')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ))

class ClassDetail(DetailView):
    model = Class 




class DivisionListView(ListView):
    template_name = 'student/student_division.html'
    model = Division

class DivisionCreate(CreateView):
    model = Division
    form_class = DivisionForm

    def get_success_url(self):
        return reverse('student_division')

    def form_valid(self, form):
        id = form.save()
        messages.success(self.request, 'Student Division Added Successfully')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ))   



class DivisionUpdate(UpdateView):
    model = Division
    form_class = DivisionForm
    


    def get_success_url(self):
        return reverse('student_division')

    def form_valid(self, form):
        id = form.save()
        messages.success(self.request, 'Student Division Added Successfully')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ))

class DivisionDetail(DetailView):
    model = Division 







    
   




   