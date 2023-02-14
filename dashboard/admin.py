from django.contrib import admin
from .models import CounselingRequest, SliderImage, Message


class CounselingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'access_code', 'pk')

    def __str__(self):
        return self.name


class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'title', 'pk', 'image')

    def __str__(self):
        return self.title


class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pay_request', 'created_at', 'pk', 'sender_id', 'receiver_id')

    def __str__(self):
        return self.title


admin.site.register(CounselingRequest, CounselingRequestAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(Message, MessageAdmin)
