# Generated by Django 4.2.4 on 2023-09-09 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0003_breed_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.breed', verbose_name='порода'),
        ),
    ]