from django.db import models


class PaymentLog(models.Model):
    invoice_id = models.CharField(max_length=255, db_index=True)
    payment_id = models.CharField(max_length=255, blank=True, default="")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=32, default="pending", db_index=True)
    raw_response = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"QPay #{self.invoice_id} ({self.status})"
