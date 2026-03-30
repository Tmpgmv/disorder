from django.db import models


class TaskMixin(models.Model):
    task = models.ForeignKey("tasks.Task",
                             on_delete=models.CASCADE,
                             related_name="%(app_label)s_%(class)s_related",
                             related_query_name="%(app_label)s_%(class)ss",
                             verbose_name="Задание")
    class Meta:
        abstract = True