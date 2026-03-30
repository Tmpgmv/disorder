from django.core.validators import MinValueValidator
from django.db import models

class Options(models.Model):
    number_of_variants = models.IntegerField(validators=[MinValueValidator(1)], default=35)
    educational_facility = models.ForeignKey("educational_facilities.EducationalFacility",
                                             on_delete=models.PROTECT,
                                             verbose_name="Учебное заведение",)

    def __str__(self):
        return "Опции"

    class Meta:
        verbose_name = "Опции"
        verbose_name_plural = "Опции"