# Generated by Django 2.2 on 2021-11-05 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rifa',
            name='comprador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Vendedor'),
        ),
    ]
