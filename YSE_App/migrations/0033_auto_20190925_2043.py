# Generated by Django 2.0.4 on 2019-09-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0032_usertelescopetofollow'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostphotdata',
            name='diffim',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='transientphotdata',
            name='diffim',
            field=models.NullBooleanField(),
        ),
    ]
