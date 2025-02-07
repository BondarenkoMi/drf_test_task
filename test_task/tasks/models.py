from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Название задачи',
        blank=False,
        null=False
        )
    description = models.TextField(
        verbose_name='Описание задачи',
        blank=True,
        null=True
        )
    due_date = models.DateField(
        verbose_name='Дата выполнения',
        blank=False,
        null=False
        )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='tasks'
        )

    def __str__(self):
        return self.title

