# Generated by Django 4.2.7 on 2024-03-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_remove_lecturecalender_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturecalender',
            name='contents',
            field=models.TextField(max_length=500, verbose_name='내용'),
        ),
    ]
