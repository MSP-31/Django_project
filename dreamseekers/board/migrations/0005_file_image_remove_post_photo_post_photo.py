# Generated by Django 4.2.7 on 2024-02-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='temp')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='temp')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ManyToManyField(to='board.image', verbose_name='이미지'),
        ),
    ]
