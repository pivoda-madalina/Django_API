# Generated by Django 3.2.8 on 2021-10-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(),
        ),
    ]