# Generated by Django 4.2.7 on 2024-03-06 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('contents', models.TextField(max_length=3000, verbose_name='내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='intro/instrs/img/', verbose_name='이미지')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
            ],
            options={
                'verbose_name': '강사진',
                'verbose_name_plural': '강사진',
                'db_table': 'intro_Instructors',
            },
        ),
    ]
