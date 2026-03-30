from django.db import models

from general.model_mixins import UnlockedMixin


def task_facility_path(instance, filename):
    return f'logo/{filename}'


class EducationalFacility(UnlockedMixin,
                          models.Model):
    superior_body_1 = models.CharField(max_length=1000,
                                       verbose_name="Вышестоящая организация 1",
                                       blank=True)
    superior_body_2 = models.CharField(max_length=1000,
                                       verbose_name="Вышестоящая организация 2",
                                       blank=True)
    formation_type = models.CharField(max_length=1000,
                                      verbose_name="Организационно-правовая форма",
                                      blank=True)
    full_name = models.CharField(max_length=1000,
                                 verbose_name="Полное наименование",
                                 blank=True)
    short_name = models.CharField(max_length=1000,
                                  verbose_name="Краткое наименование")
    logo = models.ImageField(upload_to=task_facility_path,
                             verbose_name="Логотип",
                             blank=True)

    front_page_template = models.TextField(verbose_name="Шаблон титульного листа",
                                           blank=True)

    chairperson = models.ForeignKey(
        "employees.Employee",
        on_delete=models.PROTECT,
        related_name="chairpeople",
        related_query_name="chairperson",
        verbose_name="Председатель ПЦК",
        null=True,
        blank=True,
    )
    deputy_director = models.ForeignKey(
        "employees.Employee",
        on_delete=models.PROTECT,
        related_name="deputy_directors",
        related_query_name="deputy_director",
        verbose_name="Заместитель директора по УМР",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Образовательная организация"
        verbose_name_plural = "Образовательные организации"
