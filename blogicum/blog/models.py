from django.db import models
from django.contrib.auth import get_user_model

from core.models import PublishedModel


User = get_user_model()


class Location(PublishedModel):
    name = models.CharField(
        'Название места',
        max_length=256
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self) -> str:
        return self.name[:20]


class Category(PublishedModel):
    title = models.CharField(
        'Заголовок',
        max_length=256
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text="Идентификатор страницы для URL; "
        "разрешены символы латиницы, цифры, дефис и подчёркивание."
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title[:20]


class Post(PublishedModel):
    title = models.CharField(
        'Заголовок',
        max_length=256
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text="Если установить дату и время в будущем — "
        "можно делать отложенные публикации."
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Местоположение',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self) -> str:
        return self.title[:20]
