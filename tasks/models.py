from django.db import models

from courses.model_mixins import CourseMixin
from general.model_mixins import DateTimeMixin, CommentMixin, TitleMixin, UnlockedMixin, SlugMixin, ToBeDistortedMixin, \
    ArchiveMixin
from tasks.model_mixins import TaskMixin


class TaskGroup(UnlockedMixin,
                TitleMixin,
                models.Model):
    class Meta:
        verbose_name = "Группа заданий"
        verbose_name_plural = "Группы заданий"


class Task(UnlockedMixin,
           SlugMixin,
           DateTimeMixin,
           CourseMixin,
           CommentMixin,
           TitleMixin,
           ArchiveMixin,
           models.Model):

    group = models.ForeignKey(TaskGroup,
                              on_delete=models.PROTECT,
                              null=True,
                              blank=True,
                              verbose_name="Группа заданий")
    variant = models.CharField(max_length=100,
                               verbose_name="Вариант",
                               default="",
                               blank=True, )
    threshold = models.BooleanField(default=False,
                                    verbose_name="Рубежная аттестация")
    real_demo_exam = models.BooleanField(default=False,
                                         verbose_name="Реальный пример с демонстрационного экзамена")
    exam = models.BooleanField(default=False,
                               verbose_name="Экзамен")
    inspection = models.BooleanField(default=False,
                                     verbose_name="Контрольная работа")


    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class TaskAuthor(UnlockedMixin,
                 TaskMixin,
                 models.Model):
    author = models.ForeignKey(
        "employees.Employee",
        related_name="authors",
        related_query_name="author",
        verbose_name="Автор",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.author.get_abridged_name()

    class Meta:
        verbose_name = "Автор задания"
        verbose_name_plural = "Авторы заданий"


class Distortable(UnlockedMixin,
                  TaskMixin,
                  DateTimeMixin,
                  models.Model):
    """
    Слова, которые надо искажать.
    Искажаться они будут по заданному алгоритму.
    Здесь - просто список таких слов.
    """
    word = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.task} {self.word}"

    class Meta:
        verbose_name = "Искажаемое"
        verbose_name_plural = "Искажаемое"


class Script(UnlockedMixin,
             CommentMixin,
             TaskMixin,
             DateTimeMixin,
             ToBeDistortedMixin,
             TitleMixin,
             models.Model):
    text = models.TextField(verbose_name="Скрипт")
    class Meta:
        verbose_name = "Скрипт"
        verbose_name_plural = "Скрипты"


class PrintableTask(UnlockedMixin,
                    TaskMixin,
                    DateTimeMixin,
                    CommentMixin,
                    models.Model):

    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "Распечатываемое задание"
        verbose_name_plural = "Распечатываемое задание"
