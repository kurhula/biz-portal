# Generated by Django 2.2.2 on 2019-07-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("portal", "0006_auto_20190707_1322")]

    operations = [
        migrations.AddField(
            model_name="business",
            name="cellphone_number",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="business",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="business",
            name="facebook_page_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="business",
            name="fax_number",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="business",
            name="instagram_page_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="business",
            name="phone_number",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="business",
            name="twitter_page_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="business",
            name="website_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="business",
            name="whatsapp_number",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="municipality",
            name="add_details_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="municipality",
            name="cellphone_number",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="municipality",
            name="claim_business_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="municipality",
            name="facebook_page_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="municipality",
            name="fax_number",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="municipality",
            name="instagram_page_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="municipality",
            name="phone_number",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="municipality",
            name="special_instructions",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="municipality",
            name="twitter_page_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="municipality",
            name="website_url",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="municipality",
            name="whatsapp_number",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]