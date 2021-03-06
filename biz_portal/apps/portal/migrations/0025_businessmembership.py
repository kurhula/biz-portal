# Generated by Django 2.2.2 on 2019-09-09 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("portal", "0024_merge_20190730_1201")]

    operations = [
        migrations.CreateModel(
            name="BusinessMembership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_number", models.CharField(max_length=200)),
                ("first_names", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                (
                    "membership_type",
                    models.IntegerField(
                        choices=[
                            (1, "Company Secretary"),
                            (2, "Member"),
                            (3, "Director"),
                        ]
                    ),
                ),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="members",
                        to="portal.Business",
                    ),
                ),
            ],
        )
    ]
