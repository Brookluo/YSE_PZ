# Generated by Django 2.0.4 on 2019-11-14 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0041_auto_20191114_0406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyobservation',
            name='instrument',
        ),
    ]
