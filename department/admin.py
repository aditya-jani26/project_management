from django.contrib import admin
from department.models import CustomUser,project

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display=('userName','userType')
  

class projectAdmin(admin.ModelAdmin):
    list_display=('project_Title',)


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(project,projectAdmin)
