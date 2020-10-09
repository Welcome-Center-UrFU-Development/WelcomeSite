from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    date = models.DateField(db_index=True, verbose_name='Дата')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    project = models.ForeignKey('Project', null=True, on_delete=models.PROTECT, verbose_name='Проект-организатор')

    class Meta:
        verbose_name_plural = 'Мероприятия'
        verbose_name = 'Мероприятие'
        ordering = ['-date']


class Project(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['name']
