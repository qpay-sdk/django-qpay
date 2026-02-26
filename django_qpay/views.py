import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from qpay.types import PaymentCheckRequest

from .client import get_client
from .signals import payment_received, payment_failed


@method_decorator(csrf_exempt, name="dispatch")
class WebhookView(View):
    def post(self, request):
        try:
            body = json.loads(request.body)
        except (json.JSONDecodeError, ValueError):
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        invoice_id = body.get("invoice_id")
        if not invoice_id:
            return JsonResponse({"error": "Missing invoice_id"}, status=400)

        try:
            client = get_client()
            result = client.check_payment(PaymentCheckRequest(
                object_type="INVOICE",
                object_id=invoice_id,
            ))

            if result.rows:
                payment_received.send(sender=None, invoice_id=invoice_id, result=result)
                return JsonResponse({"status": "paid"})

            payment_failed.send(sender=None, invoice_id=invoice_id, reason="No payment found")
            return JsonResponse({"status": "unpaid"})
        except Exception as e:
            payment_failed.send(sender=None, invoice_id=invoice_id, reason=str(e))
            return JsonResponse({"error": str(e)}, status=500)
