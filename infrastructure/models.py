from django.db import models

from general.model_mixins import TitleMixin, CommentMixin, UnlockedMixin


class ItemInInfrastructureList(UnlockedMixin,
                               CommentMixin,
                               models.Model):
    real_name = models.CharField(max_length=1000, verbose_name="", blank=True,
                                 default="Наименование для системного администратора")
    general_name = models.CharField(max_length=1000, verbose_name="", blank=True,
                                    default="Обобщенное наименование дя паспорта ЦПДЭ")
    okpd2 = models.CharField(max_length=1000,
                             blank=True,
                             default="",
                             verbose_name="ОКПД 2",)
    manufacturer = models.CharField(blank=True,
                                    default="",
                                    verbose_name="Производитель", )
    country = models.CharField(blank=True,
                               default="",
                               verbose_name="Страна", )


    def __str__(self):
        return self.real_name