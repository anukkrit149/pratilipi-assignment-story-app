from django.db import models
from django.contrib.postgres.fields import ArrayField


class story(models.Model):
    title = models.CharField(max_length=250)
    story = models.TextField()
    viewedBy = ArrayField(models.IntegerField(), null=True, default=list)


class logs(models.Model):
    storyId = models.IntegerField()
    userId = models.IntegerField()
    timestamp = models.DateTimeField()

