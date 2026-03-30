from django.db import models

from general.model_mixins import UnlockedMixin, SlugMixin


class Profession(UnlockedMixin,
                 SlugMixin,
                 models.Model):
    major =models.CharField(max_length=1000,
                            verbose_name="Направленность")
    name = models.CharField(max_length=1000,
                            verbose_name="Специальность")

    def __str__(self):
        return f"{self.slug} {self.name}"

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"
