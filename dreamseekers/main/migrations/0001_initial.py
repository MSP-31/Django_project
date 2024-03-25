# Generated by Django 4.2.7 on 2024-03-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('contents', models.TextField(max_length=3000, verbose_name='내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main/slide', verbose_name='이미지')),
            ],
            options={
                'verbose_name': '메인 슬라이드',
                'verbose_name_plural': '메인 슬라이드',
                'db_table': 'main_slides',
            },
        ),
    ]
