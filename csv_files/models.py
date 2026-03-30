from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models

from general.model_mixins import TitleMixin, CommentMixin, UnlockedMixin
from tasks.lib import get_task_path
from tasks.model_mixins import TaskMixin


def csv_file_path(instance, filename):
    return f'{get_task_path(instance)}/csv/{filename}'


class CsvFile(UnlockedMixin,
              TaskMixin,
              TitleMixin,
              CommentMixin,
              models.Model):
    file = models.FileField(upload_to=csv_file_path,
                            validators=[FileExtensionValidator(allowed_extensions=['csv'])],
                            verbose_name="CSV-файл")

    # Не всегда он есть.
    header_in_first_line = models.BooleanField(
        default=True,
        verbose_name="Заголовок колонок в первой строке"
    )

    class Meta:
        verbose_name = "CSV-файл"
        verbose_name_plural = "CSV-файлы"


class DistortableInCsv(UnlockedMixin,
                       CommentMixin,
                       models.Model):
    csv_file = models.ForeignKey(CsvFile,
                                 on_delete=models.CASCADE,
                                 verbose_name="CSV-файл")

    """
    Ориентироваться будем на номер колонки.
    Причина: в задании может не быть заголовка
    колонки вообще. Пример: 09.02.07 (Программист) в
    2006 году в файле Пункты выдачи_import.xlsx.
    
    Валидировать:
    Если в файле есть заголовки колонок (см. header_in_first_line в 
    CsvFile, проверить 
    соответствие фактического номера колонки введенному числу.     
   """
    column_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1), ],
        verbose_name="Номер колонки, которую искажать")

    """
    Для валидации поля column_number.
    """
    column_name = models.CharField(max_length=100,
                                   blank=True,
                                   default="",
                                   verbose_name="Заголовок колонки")

    def __str__(self):
        return f'{self.column_number} {self.column_name}'

    class Meta:
        verbose_name = "Изменяемая колонка в CSV-файле"
        verbose_name_plural = "Изменяемые колонки в CSV-файлах"
