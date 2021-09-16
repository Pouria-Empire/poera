import os

from django.db import models


def upload_to(instance, filename):
    obj = Questions.objects.latest('id')
    obj = obj.id
    print('ID', obj+1)
    return os.path.join(str(obj+1), filename)


class Questions(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    test = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.title
