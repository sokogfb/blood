# Generated by Django 2.0.6 on 2018-09-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20180818_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='info',
            name='contact_number',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
