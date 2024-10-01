# Generated by Django 5.1.1 on 2024-09-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0010_rename_desc_mechanical_credit"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mechanics",
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
                ("coarse", models.CharField(max_length=200)),
                ("desc", models.CharField(blank=True, max_length=200, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
