# Generated by Django 5.1.7 on 2025-03-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(verbose_name='опубликован')),
                ('views_count', models.IntegerField(verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
