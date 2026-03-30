from django.core.validators import FileExtensionValidator
from django.db import models

from general.model_mixins import DateTimeMixin, TitleMixin, UnlockedMixin, CommentMixin
from tasks.lib import get_task_path
from tasks.model_mixins import TaskMixin


def task_file_path(instance, filename):
    return f'{get_task_path(instance)}/file/{filename}'

class File(UnlockedMixin,
           DateTimeMixin,
           TaskMixin,
           TitleMixin,
           CommentMixin,
           models.Model):

    file = models.FileField(upload_to=task_file_path)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
