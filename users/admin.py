from django.contrib import admin
from .models import UserProfile, Role, Student, Exam, SumOfStudy


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_id', 'role', 'role_id')
    list_filter = ('role_id','user_id')


class ExamInline(admin.TabularInline):
    model = Exam
    extra = 1
    readonly_fields = ('pk','student_id')


class SumOfStudyInline(admin.TabularInline):
    model = SumOfStudy
    extra = 1
    readonly_fields = ('pk','student_id')
    ordering = ('-test_count',)


class StudentAdmin(admin.ModelAdmin):

    inlines = [ExamInline, SumOfStudyInline]
    list_display = ('student', 'major', 'grade', 'support_id','support_name', 'counselor_id', 'counselor_name', 'manager_id', 'manager_name')
    list_filter = ('major', 'grade', 'support_id', 'counselor_id', 'manager_id')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'pk')
    list_filter = ('role',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Student, StudentAdmin)


