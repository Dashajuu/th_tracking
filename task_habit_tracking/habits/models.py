from django.db import models
from django.contrib.auth.models import User

from tasks.models import Category


class Habit(models.Model):
    STATUS = [
        ('A', 'active'),
        ('F', 'finished'),
        ('S', 'stopped'),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.CharField(choices=STATUS, default='A')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='HabitCategory')


class HabitCategory(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
