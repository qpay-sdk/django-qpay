from django.conf import settings


def get_qpay_settings():
    defaults = {
        "BASE_URL": "https://merchant.qpay.mn",
        "USERNAME": "",
        "PASSWORD": "",
        "INVOICE_CODE": "",
        "CALLBACK_URL": "",
    }
    user = getattr(settings, "QPAY", {})
    return {**defaults, **user}
