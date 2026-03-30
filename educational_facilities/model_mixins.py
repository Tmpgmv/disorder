from django.db import models


class EducationalFacilityMixin(models.Model):
    educational_facility = models.ForeignKey("educational_facilities.EducationalFacility",
                                             on_delete=models.PROTECT,
                                             related_name="%(app_label)s_%(class)s_related",
                                             related_query_name="%(app_label)s_%(class)ss",
                                             verbose_name="Учебное заведение",)

    class Meta:
        abstract = True