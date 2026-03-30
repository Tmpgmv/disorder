from django.db import models


class OsMixin(models.Model):
    os = models.ForeignKey("operating_systems.OperatingSystem",
                           related_name="%(app_label)s_%(class)s_related",
                           related_query_name="%(app_label)s_%(class)ss",
                           on_delete=models.PROTECT,
                           verbose_name="Операционная система")

    class Meta:
        abstract = True
