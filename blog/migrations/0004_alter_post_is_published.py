# Generated by Django 5.1.7 on 2025-03-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликован'),
        ),
    ]
