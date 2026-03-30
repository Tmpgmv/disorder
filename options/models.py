from django.core.validators import MinValueValidator
from django.db import models

from courses.model_mixins import CourseMixin
from educational_facilities.model_mixins import EducationalFacilityMixin
from operating_systems.model_mixins import OsMixin


class Options(CourseMixin,
              EducationalFacilityMixin,
              OsMixin,
              models.Model):
    number_of_variants = models.IntegerField(validators=[MinValueValidator(1)], default=35)

    def __str__(self):
        return "Опции"

    class Meta:
        verbose_name = "Опции"
        verbose_name_plural = "Опции"