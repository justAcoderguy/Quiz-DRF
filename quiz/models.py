from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(str):
        return self.name

class Quizzes(models.Model):

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']

    title = models.CharField(max_length-255, default=_('New Quiz'), verbose_name=_('Quiz Title')
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)

class Question(Updated):
    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)

class Answer(Updated):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
