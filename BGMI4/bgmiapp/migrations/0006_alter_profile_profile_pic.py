# Generated by Django 3.2 on 2021-06-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgmiapp', '0005_squad_21_6_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profiles_pic'),
        ),
    ]