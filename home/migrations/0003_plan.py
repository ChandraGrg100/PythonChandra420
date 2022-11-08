# Generated by Django 4.1.1 on 2022-09-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_feedback_alter_contact_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plan",
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
                ("economy", models.IntegerField()),
                ("business", models.IntegerField()),
                ("premium", models.IntegerField()),
                ("exculsive", models.IntegerField()),
            ],
        ),
    ]
