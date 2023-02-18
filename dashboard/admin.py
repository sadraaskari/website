from django.contrib import admin
from .models import CounselingRequest, SliderImage, Ticket, Option, SendSMS
from .forms import SendSMSForm, TicketForm
from users.models import UserProfile


class CounselingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'access_code', 'pk')
    ordering = ('-created_at',)

    def __str__(self):
        return self.name


class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'title', 'pk', 'image')

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


class TicketAdmin(admin.ModelAdmin):
    form = TicketForm
    list_display = ('title', 'pay_request', 'created_at', 'sender', 'receiver', 'pk')


admin.site.register(CounselingRequest, CounselingRequestAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(SendSMS, SendSMSAdmin)
