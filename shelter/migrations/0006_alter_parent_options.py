# Generated by Django 4.2.4 on 2023-09-24 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0005_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parent',
            options={'verbose_name': 'предок', 'verbose_name_plural': 'предки'},
        ),
    ]
