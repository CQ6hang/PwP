import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    nickname = models.CharField(max_length=20)
    gender = models.BooleanField(default=0)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    birth = models.DateTimeField('birthday', default=timezone.now())
    headPic = models.CharField(max_length=200, default="/img/head/default_img.png")

    # token = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img_path = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.description

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s_time = models.DateTimeField('task submit time')
    c_time = models.IntegerField()
    progress = models.FloatField()
    state = models.BooleanField()


class Suggester(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Suggestion(models.Model):
    suggester = models.ForeignKey(Suggester, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
