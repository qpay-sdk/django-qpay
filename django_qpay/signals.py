from django.dispatch import Signal

payment_received = Signal()  # sender=None, payment_id, result
payment_failed = Signal()    # sender=None, payment_id, reason
