# Generated by Django 3.2 on 2021-06-22 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubg_id', models.PositiveIntegerField(blank=True, null=True)),
                ('pubg_name', models.CharField(blank=True, max_length=15, null=True)),
                ('phone_no', models.PositiveIntegerField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='img/profiles/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='solo_21_6_2021',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_pubg_id', models.PositiveIntegerField()),
                ('player1_pubg_name', models.CharField(max_length=15)),
                ('bgmiuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgmiapp.profile')),
            ],
        ),
    ]
