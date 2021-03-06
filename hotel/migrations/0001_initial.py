# Generated by Django 3.2.3 on 2021-05-23 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('cityCode', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('cityName', models.CharField(max_length=100)),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelCode', models.CharField(max_length=10)),
                ('hotelName', models.CharField(max_length=200)),
                ('updated', models.DateTimeField()),
                ('cityCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.city')),
            ],
        ),
    ]
