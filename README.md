# django-qpay

[![PyPI](https://img.shields.io/pypi/v/django-qpay)](https://pypi.org/project/django-qpay/)
[![CI](https://github.com/qpay-sdk/django-qpay/actions/workflows/ci.yml/badge.svg)](https://github.com/qpay-sdk/django-qpay/actions)

QPay V2 payment integration for Django.

## Install

```bash
pip install django-qpay
```

Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "django_qpay",
]
```

## Configuration

```python
# settings.py
QPAY = {
    "BASE_URL": "https://merchant.qpay.mn",
    "USERNAME": "your_username",
    "PASSWORD": "your_password",
    "INVOICE_CODE": "your_invoice_code",
    "CALLBACK_URL": "https://yoursite.com/qpay/webhook/",
}
```

## URLs

```python
urlpatterns = [
    path("qpay/", include("django_qpay.urls")),
]
```

## Usage

```python
from django_qpay.client import get_client
from qpay.types import CreateSimpleInvoiceRequest

client = get_client()
invoice = client.create_simple_invoice(CreateSimpleInvoiceRequest(
    invoice_code="YOUR_CODE",
    sender_invoice_no="ORDER-001",
    amount=10000,
    callback_url="https://yoursite.com/qpay/webhook/",
))
```

## Template Tags

```html
{% load qpay_tags %}
{% qpay_qr invoice.qr_image %}
{% qpay_payment_links invoice.urls %}
```

## Signals

```python
from django_qpay.signals import payment_received

@receiver(payment_received)
def on_payment(sender, invoice_id, result, **kwargs):
    ...
```

## License

MIT
