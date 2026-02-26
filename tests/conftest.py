import django
from django.conf import settings


def pytest_configure():
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "django_qpay",
        ],
        QPAY={
            "BASE_URL": "https://merchant-sandbox.qpay.mn",
            "USERNAME": "test_user",
            "PASSWORD": "test_pass",
            "INVOICE_CODE": "TEST_INVOICE",
            "CALLBACK_URL": "https://example.com/callback",
        },
    )
    django.setup()
