from django.db import models

from courses.model_mixins import CourseMixin
from general.model_mixins import CommentMixin, UnlockedMixin, ArchiveMixin
from operating_systems.model_mixins import OsMixin




class InfrastructureListForPassport(UnlockedMixin,
                                    OsMixin,
                                    CourseMixin,
                                    ArchiveMixin,
                                    CommentMixin,
                                    models.Model):
    general_name = models.CharField(max_length=1000, verbose_name="", blank=True,
                                    default="Обобщенное наименование дя паспорта ЦПДЭ")
    okpd2 = models.CharField(max_length=1000,
                             blank=True,
                             default="",
                             verbose_name="ОКПД 2", )
    manufacturer = models.CharField(blank=True,
                                    default="",
                                    verbose_name="Производитель", )
    country = models.CharField(blank=True,
                               default="",
                               verbose_name="Страна", )

    def __str__(self):
        return self.general_name


class InfrastructureListForAdmin(UnlockedMixin,
                                 OsMixin,
                                 CourseMixin,
                                 ArchiveMixin,
                                 CommentMixin,
                                 models.Model):
    real_name = models.CharField(max_length=1000,
                                 verbose_name="Наименование для системного администратора", blank=True,
                                 default="")
    download_link = models.CharField(max_length=1000,
                                     blank=True,
                                     default="",
                                     verbose_name="Ссылка для скачивания")

    instruction = models.TextField(blank=True,
                                   default="",
                                   verbose_name="Инструкция по установке")

    def __str__(self):
        return self.real_name
