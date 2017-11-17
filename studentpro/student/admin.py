from django.contrib import admin

# Register your models here.
from .models import StudentTable,Class,Division

admin.site.register(StudentTable)
admin.site.register(Class)
admin.site.register(Division)