from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def qpay_qr(qr_image, size=256):
    if not qr_image:
        return ""
    html = (
        f'<div class="qpay-qr-code" style="text-align:center;">'
        f'<img src="data:image/png;base64,{qr_image}" '
        f'alt="QPay QR Code" width="{size}" height="{size}">'
        f'</div>'
    )
    return mark_safe(html)


@register.simple_tag
def qpay_payment_links(urls):
    if not urls:
        return ""
    items = []
    for link in urls:
        logo = link.get("logo", "")
        name = link.get("name", "Pay")
        href = link.get("link", "#")
        logo_html = f'<img src="{logo}" width="24" height="24" alt="{name}"> ' if logo else ""
        items.append(
            f'<a href="{href}" target="_blank" '
            f'style="display:inline-flex;align-items:center;gap:6px;padding:10px 16px;'
            f'border:1px solid #ddd;border-radius:8px;text-decoration:none;color:#333;font-size:14px;">'
            f'{logo_html}{name}</a>'
        )
    html = f'<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;">{"".join(items)}</div>'
    return mark_safe(html)
