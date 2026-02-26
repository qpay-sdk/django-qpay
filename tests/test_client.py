from unittest.mock import patch, MagicMock

from django_qpay import client as client_module
from django_qpay.client import get_client


class TestGetClient:
    def setup_method(self):
        client_module._client = None

    def teardown_method(self):
        client_module._client = None

    @patch("django_qpay.client.QPayClient")
    @patch("django_qpay.client.QPayConfig")
    def test_creates_client(self, mock_config_cls, mock_client_cls):
        mock_config = MagicMock()
        mock_config_cls.return_value = mock_config
        mock_client = MagicMock()
        mock_client_cls.return_value = mock_client

        result = get_client()

        mock_config_cls.assert_called_once()
        mock_client_cls.assert_called_once_with(mock_config)
        assert result is mock_client

    @patch("django_qpay.client.QPayClient")
    @patch("django_qpay.client.QPayConfig")
    def test_returns_singleton(self, mock_config_cls, mock_client_cls):
        mock_client = MagicMock()
        mock_client_cls.return_value = mock_client

        first = get_client()
        second = get_client()

        assert first is second
        assert mock_client_cls.call_count == 1

    @patch("django_qpay.client.QPayClient")
    @patch("django_qpay.client.QPayConfig")
    def test_passes_settings_to_config(self, mock_config_cls, mock_client_cls):
        get_client()

        call_kwargs = mock_config_cls.call_args
        assert call_kwargs[1]["base_url"] == "https://merchant-sandbox.qpay.mn"
        assert call_kwargs[1]["username"] == "test_user"
        assert call_kwargs[1]["password"] == "test_pass"
        assert call_kwargs[1]["invoice_code"] == "TEST_INVOICE"
        assert call_kwargs[1]["callback_url"] == "https://example.com/callback"
