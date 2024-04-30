# Generated by Django 5.0.4 on 2024-04-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
            ],
        ),
    ]
