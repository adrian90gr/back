# Generated by Django 5.0.6 on 2024-06-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='id',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(default='DefaultCategoria', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='matricula',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
