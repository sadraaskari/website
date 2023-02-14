from django.contrib import admin
from .models import CounselingRequest


class CounselingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'access_code', 'pk')

    def __str__(self):
        return self.name


admin.site.register(CounselingRequest, CounselingRequestAdmin)
