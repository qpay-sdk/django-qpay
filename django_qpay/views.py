from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from qpay.types import PaymentCheckRequest

from .client import get_client
from .signals import payment_received, payment_failed


@method_decorator(csrf_exempt, name="dispatch")
class WebhookView(View):
    """QPay callback handler.

    QPay sends a GET request with ``qpay_payment_id`` as a query parameter.
    The handler verifies the payment via ``check_payment()`` and returns
    ``SUCCESS`` as plain text (HTTP 200).
    """

    def get(self, request):
        payment_id = request.GET.get("qpay_payment_id")
        if not payment_id:
            return HttpResponse(
                "Missing qpay_payment_id", status=400, content_type="text/plain"
            )

        try:
            client = get_client()
            result = client.check_payment(PaymentCheckRequest(
                object_type="INVOICE",
                object_id=payment_id,
            ))

            if result.rows:
                payment_received.send(
                    sender=None, payment_id=payment_id, result=result
                )
                return HttpResponse("SUCCESS", status=200, content_type="text/plain")

            payment_failed.send(
                sender=None, payment_id=payment_id, reason="No payment found"
            )
            return HttpResponse("FAILED", status=200, content_type="text/plain")
        except Exception as e:
            payment_failed.send(
                sender=None, payment_id=payment_id, reason=str(e)
            )
            return HttpResponse("ERROR", status=500, content_type="text/plain")
