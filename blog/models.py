from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(**NULLABLE, max_length=100, verbose_name='slug')
    body = models.TextField(**NULLABLE, verbose_name='содержимое')
    image = models.ImageField(upload_to='posts/', **NULLABLE, verbose_name='изображение')
    create_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='опубликован', default=True)
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


