from django.db import models

from general.model_mixins import UnlockedMixin


class Employee(UnlockedMixin,
               models.Model):
    first_name = models.CharField(max_length=100,
                                  verbose_name="Имя")
    patronymic = models.CharField(max_length=100,
                                  verbose_name="Отчество")
    last_name = models.CharField(max_length=100,
                                 verbose_name="Фамилия")
    degree = models.CharField(max_length=100,
                              blank=True,
                              default='',
                              verbose_name="Ученая степень")

    def get_abridged_name(self):
        return f'{self.degree} {self.first_name[0]}. {self.patronymic[0]}. {self.last_name}'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
