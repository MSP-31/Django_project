# Generated by Django 4.2.7 on 2024-06-19 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0008_intro'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='businessinfo',
            table='intro_business_info',
        ),
        migrations.AlterModelTable(
            name='contact',
            table='intro_contact',
        ),
        migrations.AlterModelTable(
            name='instructors',
            table='intro_instructors',
        ),
        migrations.AlterModelTable(
            name='intro',
            table='intro_intro',
        ),
    ]
