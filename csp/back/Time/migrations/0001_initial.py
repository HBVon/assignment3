# Generated by Django 5.0.6 on 2024-06-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TTSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('module_name', models.CharField(max_length=100)),
                ('teacher_name', models.CharField(max_length=100)),
                ('group_name', models.CharField(max_length=100)),
                ('classroom_name', models.CharField(max_length=100)),
            ],
        ),
    ]
