# Generated by Django 3.2.3 on 2021-05-27 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0002_auto_20210524_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='managers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.city')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
