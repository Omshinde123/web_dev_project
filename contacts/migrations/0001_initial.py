# Generated by Django 4.1.2 on 2022-10-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacts",
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
                ("Name", models.CharField(max_length=100)),
                ("Email", models.CharField(max_length=50)),
                ("Message", models.CharField(blank=True, max_length=100, null=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name_plural": "Contacts",},
        ),
    ]
