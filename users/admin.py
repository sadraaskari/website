from django.contrib import admin
from .models import UserProfile
from .models import Student
from .models import Role


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_id', 'role', 'role_id')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role)
admin.site.register(Student)

