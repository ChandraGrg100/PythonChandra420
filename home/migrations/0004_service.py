# Generated by Django 4.1.1 on 2022-09-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_plan"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=100)),
                ("icon", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
    ]
