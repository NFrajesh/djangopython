# Generated by Django 3.2 on 2021-06-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgmiapp', '0011_auto_20210627_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo_21_6_2021',
            name='form_submited',
            field=models.BooleanField(default=False),
        ),
    ]