# Generated by Django 3.1.4 on 2021-01-04 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OtatesApp', '0004_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='sucursale',
            new_name='sucursal',
        ),
    ]