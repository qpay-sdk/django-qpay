from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PaymentLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("invoice_id", models.CharField(db_index=True, max_length=255)),
                ("payment_id", models.CharField(blank=True, default="", max_length=255)),
                ("amount", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("status", models.CharField(db_index=True, default="pending", max_length=32)),
                ("raw_response", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
