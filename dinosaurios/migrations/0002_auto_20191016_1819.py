# Generated by Django 2.2.6 on 2019-10-16 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='dinosaurio',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinosaurios.Periodo', verbose_name='Periodo'),
        ),
    ]
