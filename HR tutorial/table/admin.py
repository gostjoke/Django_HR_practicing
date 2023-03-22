from django.contrib import admin
from .models import employee, vaction, department

# Register your models here.

class employeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'name','apartment_name')

class vactionAdmin(admin.ModelAdmin):
    list_display = ('emp_id','vaction_start','vaction_end','vaction_length')
    # exclude =()

class departmentAdmin(admin.ModelAdmin):
    list_display = ('dpartment_name', 'apartment_information') 

admin.site.register(employee, employeeAdmin)
admin.site.register(vaction, vactionAdmin)
admin.site.register(department, departmentAdmin)