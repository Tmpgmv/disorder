from django.db import models


class UnlockedMixin(models.Model):
    unlocked = models.BooleanField(default=False,
                                   verbose_name="Предохранитель снят")

    class Meta:
        abstract = True


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Дата редактирования")

    class Meta:
        abstract = True


class CommentMixin(models.Model):
    comment = models.TextField(blank=True,
                               default='',
                               verbose_name="Комментарий")

    class Meta:
        abstract = True


class TitleMixin(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Наименование")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title}"


class SlugMixin(models.Model):
    slug = models.CharField(max_length=100,
                            blank=True,
                            default='',
                            verbose_name="Код")

    class Meta:
        abstract = True


class ToBeDistortedMixin(models.Model):
    to_be_distorted = models.BooleanField(default=True,
                                          verbose_name="Искажать")

    class Meta:
        abstract = True


class ArchiveMixin(models.Model):
    archive = models.BooleanField(default=False,
                                  verbose_name="Архив")

    class Meta:
        abstract = True
