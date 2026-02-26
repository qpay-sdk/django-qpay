from django.urls import path

from .views import WebhookView

app_name = "django_qpay"

urlpatterns = [
    path("webhook/", WebhookView.as_view(), name="webhook"),
]
