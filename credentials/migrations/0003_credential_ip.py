# Generated by Django 4.0.5 on 2022-06-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0002_rename_credentials_credential'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='ip',
            field=models.CharField(default='127.0.0.1', max_length=15),
            preserve_default=False,
        ),
    ]
