# Generated by Django 3.2 on 2021-09-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte02', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContratosHc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mpmeni', models.CharField(max_length=15)),
                ('menomb', models.CharField(max_length=30)),
            ],
        ),
    ]
