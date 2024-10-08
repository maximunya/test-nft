# Generated by Django 5.1 on 2024-08-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "unique_hash",
                    models.CharField(editable=False, max_length=20, unique=True),
                ),
                ("tx_hash", models.CharField(max_length=66, unique=True)),
                ("media_url", models.URLField()),
                ("owner", models.CharField(max_length=42)),
            ],
            options={
                "verbose_name": "Token",
                "verbose_name_plural": "Tokens",
            },
        ),
    ]
