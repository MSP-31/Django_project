# Generated by Django 4.2.7 on 2024-04-03 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='file')),
            ],
            options={
                'db_table': 'community_archive_file',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'db_table': 'community_archive_imgs',
            },
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('contents', models.TextField(max_length=3000, verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='수정일')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_Archive', to=settings.AUTH_USER_MODEL, verbose_name='글쓴이')),
                ('files', models.ManyToManyField(blank=True, to='archive.file', verbose_name='파일')),
                ('image', models.ManyToManyField(blank=True, to='archive.image', verbose_name='이미지')),
            ],
            options={
                'verbose_name': '자료실',
                'verbose_name_plural': '자료실',
                'db_table': 'community_archive',
            },
        ),
    ]
