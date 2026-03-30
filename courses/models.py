from django.db import models

from general.model_mixins import DateTimeMixin, CommentMixin, TitleMixin, UnlockedMixin, SlugMixin


class Course(UnlockedMixin,
             SlugMixin,
             DateTimeMixin,
             CommentMixin,
             TitleMixin,
             models.Model):
    profession = models.ForeignKey("professions.Profession",
                                   on_delete=models.PROTECT,
                                   verbose_name="Специальность")
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
