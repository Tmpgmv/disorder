from django.core.validators import MinValueValidator
from django.db import models

from general.model_mixins import UnlockedMixin, DateTimeMixin, CommentMixin, TitleMixin, ToBeDistortedMixin
from tasks.lib import get_task_path
from tasks.model_mixins import TaskMixin


def task_image_path(instance, filename):
    return f'{get_task_path(instance)}/img/{filename}'


class Img(UnlockedMixin,
          DateTimeMixin,
          TaskMixin,
          TitleMixin,
          ToBeDistortedMixin,
          CommentMixin,
          models.Model):
    """
    Наименование файла с изображением надо искажать сообразно
    новому названию в csv-файле.
    """

    csv = models.ForeignKey("csv_files.CsvFile",
                            on_delete=models.PROTECT,
                            related_name="%(app_label)s_%(class)s_related",
                            related_query_name="%(app_label)s_%(class)ss",
                            verbose_name="CSV-файл",
                            blank=True,
                            )

    column_number = models.PositiveIntegerField(default=0,
                                                validators=[MinValueValidator(1),],
                                                blank=True,
                                                verbose_name="Для искажения найти в колонке")

    image = models.ImageField(upload_to=task_image_path, verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
