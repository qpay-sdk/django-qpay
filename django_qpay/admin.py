from django.contrib import admin

from .models import PaymentLog


@admin.register(PaymentLog)
class PaymentLogAdmin(admin.ModelAdmin):
    list_display = ["invoice_id", "payment_id", "amount", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["invoice_id", "payment_id"]
    readonly_fields = ["created_at", "updated_at"]
