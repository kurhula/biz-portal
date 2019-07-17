# Generated by Django 2.2.2 on 2019-07-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("portal", "0009_auto_20190712_1327")]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="annual_turnover",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Less than R100,000"),
                    (2, "R100,000 to R500,000"),
                    (3, "R500,000 to R1,500,000"),
                    (4, "R1,500,000 to R5,000,000"),
                    (5, "More than R5,000,000"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="business",
            name="number_employed",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
