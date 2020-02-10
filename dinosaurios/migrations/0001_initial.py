# Generated by Django 2.2.6 on 2019-10-14 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dinosaurio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagen', models.ImageField(upload_to=None, verbose_name='Imágen')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinosaurios.Periodo', verbose_name='periodo_fk')),
            ],
        ),
    ]
