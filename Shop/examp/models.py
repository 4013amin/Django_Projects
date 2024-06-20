from django.db import models


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
