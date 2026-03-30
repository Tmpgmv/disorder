from django.db import models

from general.model_mixins import DateTimeMixin, CommentMixin, TitleMixin, UnlockedMixin, SlugMixin


class Course(UnlockedMixin,
             SlugMixin,
             DateTimeMixin,
             CommentMixin,
             TitleMixin,
             models.Model):
    profession = models.ForeignKey("professions.Profession",
                                   on_delete=models.PROTECT,
                                   verbose_name="Специальность")

    instruction_on_room_preparation = models.TextField(verbose_name="Как оснастить кабинет")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class CoursesInFacilities(UnlockedMixin,
                          models.Model):
    """
    Модель необходима для сведения воедино инфраструктурного
    листа по образовательному учреждению.

    Это необходимо для подачи руководству образовательного учреждения
    сведений о необходимом оснащении кабинетов.
    """


    course = models.ForeignKey("courses.Course",
                               on_delete=models.PROTECT,
                               verbose_name="Курс")

    facility = models.ForeignKey("educational_facilities.EducationalFacility",
                               on_delete=models.PROTECT,
                               verbose_name="Образовательное учреждение")

    def __str__(self):
        return f"{self.facility} - {self.course}"


    class Meta:
        verbose_name = "Курс в образовательном учреждении"
        verbose_name_plural = "Курсы в образовательных учреждениях"


