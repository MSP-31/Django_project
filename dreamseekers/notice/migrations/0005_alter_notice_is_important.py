# Generated by Django 4.2.7 on 2024-05-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_notice_is_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='is_important',
            field=models.BooleanField(default=False, verbose_name='중요공지'),
        ),
    ]
