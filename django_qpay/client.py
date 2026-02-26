from qpay import QPayClient, QPayConfig

from .settings import get_qpay_settings

_client = None


def get_client() -> QPayClient:
    global _client
    if _client is None:
        s = get_qpay_settings()
        config = QPayConfig(
            base_url=s["BASE_URL"],
            username=s["USERNAME"],
            password=s["PASSWORD"],
            invoice_code=s["INVOICE_CODE"],
            callback_url=s["CALLBACK_URL"],
        )
        _client = QPayClient(config)
    return _client
