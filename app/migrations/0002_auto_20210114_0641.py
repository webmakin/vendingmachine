# Generated by Django 3.1.5 on 2021-01-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attempt',
            name='change_returned',
        ),
        migrations.AddField(
            model_name='purchase',
            name='change_returned',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
