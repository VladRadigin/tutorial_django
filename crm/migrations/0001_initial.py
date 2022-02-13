# Generated by Django 4.0.2 on 2022-02-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateField(auto_now=True)),
                ('order_name', models.CharField(max_length=120)),
                ('order_phone', models.CharField(max_length=120)),
            ],
        ),
    ]
