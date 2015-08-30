from django.db import models


class List(models.Model):
  pass


class Task(models.Model):
  description = models.TextField()
  list = models.ForeignKey(List, default=None)
