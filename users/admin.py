from django.contrib import admin
from .models import UserProfile
from .models import Student
from .models import Role


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_id', 'role', 'role_id')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'major', 'grade', 'support_id','support_name', 'counselor_id', 'counselor_name', 'manager_id', 'manager_name')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role)
admin.site.register(Student, StudentAdmin)

