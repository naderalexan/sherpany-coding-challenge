# Generated by Django 3.0.5 on 2020-05-01 13:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20200501_1141'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together={('user', 'event')},
        ),
    ]