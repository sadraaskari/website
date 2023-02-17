from django.contrib import admin
from .models import Payment
from .models import Division
from .models import Transaction


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'created_at', 'pk')
    ordering = ('-created_at',)
    list_filter = ('student_id',)

    def __str__(self):
        return self.student.student.username


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'created_at', 'pk')
    ordering = ('-created_at',)

    def user_id(self, obj):
        return obj.transaction_user.user_id

    def __str__(self):
        return self.transaction_user.user.username


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Division)
admin.site.register(Transaction, TransactionAdmin)