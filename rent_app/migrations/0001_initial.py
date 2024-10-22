# Generated by Django 5.1.2 on 2024-10-19 10:02

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='car_images/')),
                ('phone_number', models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+91 999999999'. Up to 10 digits allowed.", regex='^\\+?91?\\d{10,15}$')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.TextField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]