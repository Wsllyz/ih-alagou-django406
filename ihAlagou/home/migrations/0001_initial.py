# Generated by Django 4.0.6 on 2024-08-22 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distancia', models.IntegerField()),
                ('temperatura', models.IntegerField()),
                ('statusBateria', models.IntegerField()),
                ('timestamp', models.TextField()),
            ],
        ),
    ]
