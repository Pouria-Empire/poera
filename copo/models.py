import os

from django.db import models

from django.conf import settings


def upload_to_in(instance, filename):
    obj = Questions.objects.latest('id')
    obj = obj.id
    print('ID', obj + 1)
    return os.path.join(str(obj + 1), 'in.txt')


def upload_to_out(instance, filename):
    obj = Questions.objects.latest('id')
    obj = obj.id
    print('ID', obj + 1)
    return os.path.join(str(obj + 1), 'ex_out.txt')


class Questions(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    in_txt = models.FileField(upload_to=upload_to_in)
    out_txt = models.FileField(upload_to=upload_to_out)

    def __str__(self):
        return self.title


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=0, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
