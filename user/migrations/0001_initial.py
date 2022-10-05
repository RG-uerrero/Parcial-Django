# Generated by Django 4.1.1 on 2022-09-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('eid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('elastname', models.CharField(max_length=100)),
                ('eage', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('frecuencia_cardiaca', models.CharField(max_length=100)),
                ('saturacion_oxigeno', models.CharField(max_length=100)),
                ('nivel_stress', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]