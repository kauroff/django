# Generated by Django 5.1.7 on 2025-03-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]
