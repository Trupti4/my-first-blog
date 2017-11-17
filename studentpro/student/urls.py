from django.conf.urls import url
from student import views

urlpatterns = [
	
	url(r'^$', views.HomeTemplateView.as_view(), name='home'),
	url(r'^student/$', views.StudentTableListView.as_view(), name='student'),
	url(r'^add_student/$', views.StudentTableCreate.as_view(), name='add_student'),
	url(r'^edit-student/(?P<pk>\d+)$', views.StudentTableUpdate.as_view(), name='edit-student'),
	url(r'^view-student/(?P<pk>\d+)$', views.StudentTableDetail.as_view(), name='view-student'),
	
	url(r'^student_class/$', views.ClassListView.as_view(), name='student_class'),
	url(r'^add_studentclass/$', views.ClassCreate.as_view(), name='add_studentclass'),
	url(r'^edit-student-class/(?P<pk>\d+)$', views.ClassUpdate.as_view(), name='edit-student-class'),
	url(r'^view-student-class/(?P<pk>\d+)$', views.ClassDetail.as_view(), name='view-student-class'),

	url(r'^student_division/$', views.DivisionListView.as_view(), name='student_division'),
	url(r'^add_studentdivision/$', views.DivisionCreate.as_view(), name='add_studentdivision'),
	url(r'^edit-student-division/(?P<pk>\d+)$', views.DivisionUpdate.as_view(), name='edit-student-division'),
	url(r'^view-student-division/(?P<pk>\d+)$', views.DivisionDetail.as_view(), name='view-student-division'),




]	