from django.contrib import admin
from .models import UserProfile, Role, Student, Exam, SumOfStudy

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_id', 'role', 'role_id')


class ExamInline(admin.TabularInline):
    model = Exam
    extra = 1
    readonly_fields = ('pk',)


class SumOfStudyInline(admin.TabularInline):
    model = SumOfStudy
    extra = 1
    readonly_fields = ('pk',)


class StudentAdmin(admin.ModelAdmin):

    inlines = [ExamInline, SumOfStudyInline]
    list_display = ('student', 'major', 'grade', 'support_id','support_name', 'counselor_id', 'counselor_name', 'manager_id', 'manager_name')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role)
admin.site.register(Student, StudentAdmin)
