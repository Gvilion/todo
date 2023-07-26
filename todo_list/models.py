from django.db import models


class Task(models.Model):
    content = models.fields.TextField()
    datetime = models.fields.DateTimeField(auto_now_add=True)
    deadline = models.fields.DateTimeField(null=True)
    done = models.fields.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")


class Tag(models.Model):
    name = models.fields.CharField()
