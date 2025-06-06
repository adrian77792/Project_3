# Generated by Django 5.2.1 on 2025-05-26 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True)),
                ('photo', models.URLField(blank=True)),
                ('duration', models.IntegerField(help_text='Time Duration in Minutes')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subservice', to='main.service')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
