from django.db import models

from general.model_mixins import TitleMixin, CommentMixin, UnlockedMixin


class OperatingSystem(UnlockedMixin,
                      TitleMixin,
                      CommentMixin,
                      models.Model):
    pass
