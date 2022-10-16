from django.contrib import admin

# Register your models here.

from MyApp.models import Employee

admin.site.register(Employee)

from MyApp.models import TestTable

admin.site.register(TestTable)


