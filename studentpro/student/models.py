from django.db import models

#Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.class_name

class Division(models.Model):
    stud_class = models.ForeignKey(Class)
    division_name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.division_name


class StudentTable(models.Model):

	student_ID = models.CharField(max_length=100, primary_key=True)
	roll_no = models.CharField(max_length=100)
	student_name = models.CharField(max_length=100)
	division = models.ForeignKey(Division)
	student_class = models.ForeignKey(Class)

	class Meta:
		ordering = ['student_ID']
		
	
	def __str__(self):
		return  str(self.student_ID) + " - " + self.student_name


			