# Generated by Django 3.1.4 on 2021-01-04 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OtatesApp', '0007_auto_20210104_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OtatesApp.sucursal'),
        ),
    ]