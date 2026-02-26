from django_qpay.settings import get_qpay_settings


class TestGetQPaySettings:
    def test_returns_dict(self):
        result = get_qpay_settings()
        assert isinstance(result, dict)

    def test_has_required_keys(self):
        result = get_qpay_settings()
        expected_keys = {"BASE_URL", "USERNAME", "PASSWORD", "INVOICE_CODE", "CALLBACK_URL"}
        assert expected_keys.issubset(result.keys())

    def test_loads_from_django_settings(self):
        result = get_qpay_settings()
        assert result["BASE_URL"] == "https://merchant-sandbox.qpay.mn"
        assert result["USERNAME"] == "test_user"
        assert result["PASSWORD"] == "test_pass"
        assert result["INVOICE_CODE"] == "TEST_INVOICE"
        assert result["CALLBACK_URL"] == "https://example.com/callback"

    def test_defaults_when_no_qpay_setting(self, settings):
        delattr(settings, "QPAY")
        result = get_qpay_settings()
        assert result["BASE_URL"] == "https://merchant.qpay.mn"
        assert result["USERNAME"] == ""
        assert result["PASSWORD"] == ""
        assert result["INVOICE_CODE"] == ""
        assert result["CALLBACK_URL"] == ""
