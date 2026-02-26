from django.dispatch import Signal

payment_received = Signal()  # sender=None, invoice_id, result
payment_failed = Signal()    # sender=None, invoice_id, reason
