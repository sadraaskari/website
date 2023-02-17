from django.contrib import admin
from .models import CounselingRequest, SliderImage, Message, Option, SendSMS
from .forms import SendSMSForm


class CounselingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'access_code', 'pk')
    ordering = ('-created_at',)

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


class OptionAdmin(admin.ModelAdmin):
    list_display = ('option_key', 'option_value', 'created_at', 'pk')

    def __str__(self):
        return self.option_key


class SendSMSAdmin(admin.ModelAdmin):

    form = SendSMSForm
    list_display = ('text', 'pk')
    actions = ['clean']


admin.site.register(CounselingRequest, CounselingRequestAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(SendSMS, SendSMSAdmin)
