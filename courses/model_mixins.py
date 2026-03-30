from django.db import models


class CourseMixin(models.Model):
    course = models.ForeignKey("courses.Course",
                               on_delete=models.PROTECT,
                               related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss",
                               verbose_name="Курс")

    class Meta:
        abstract = True
