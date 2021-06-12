from djongo import models


class Question(models.Model):
    number = models.IntegerField()
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
