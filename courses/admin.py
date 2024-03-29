from django.contrib import admin
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('tutorial_name', 'tutorial_type', 'creator_id', 'status', 'created_at', 'pk')
    list_filter = ('tutorial_type', 'status')


admin.site.register(Tutorial, TutorialAdmin)
