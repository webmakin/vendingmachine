# Generated by Django 3.1.5 on 2021-01-13 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product_purchased', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins_inserted', models.CharField(max_length=300)),
                ('change_returned', models.CharField(max_length=300)),
                ('product_selected', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.product')),
            ],
        ),
    ]
