# Generated by Django 5.1.1 on 2024-09-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_rename_grades_credit_desc"),
    ]

    operations = [
        migrations.CreateModel(
            name="Desc",
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
                ("desc", models.TextField(blank=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
