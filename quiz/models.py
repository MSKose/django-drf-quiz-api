from django.db import models

#! see https://docs.djangoproject.com/en/4.0/topics/i18n/translation/ for this import's duty
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quizzes(models.Model):
    #! we don't want to anything if a quiz is deleted, thus the on_delete=models.DO_NOTHING part
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']

class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        #! for Abstract base classes see: https://docs.djangoproject.com/en/4.1/topics/db/models/#abstract-base-classes
        abstract = True

class Question(Updated):
    SCALE = (
        (0, _("Fundamental")),
        (1, _("Beginner")),
        (2, _("Intermediate")),
        (3, _("Advanced")),
        (4, _("Expert"))
    )

    TYPE = (
        (0, _("Multiple Choice")),
    )

    quiz = models.ForeignKey(Quizzes, related_name="question", on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of Question"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    def __str__(self):
        return self.title

class Answer(Updated):
    question = models.ForeignKey(Question, related_name="answer", on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    def __str__(self):
        return self.answer_text