# Generated by Django 2.0.2 on 2018-04-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='blood_types',
            field=models.CharField(choices=[('1', 'A+'), ('2', 'B+'), ('3', 'A-'), ('4', 'B-'), ('5', 'AB+'), ('6', 'AB-'), ('7', 'O+'), ('8', 'O-')], max_length=5),
        ),
        migrations.AlterField(
            model_name='info',
            name='contact_number',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
