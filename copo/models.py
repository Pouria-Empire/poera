import os

from django.db import models


def upload_to(instance, filename):
    print('ID', instance.id)
    return os.path.join(str(instance.id), filename)


class Questions(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    test = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.title
