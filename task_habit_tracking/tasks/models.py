from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY = [
        ('DO', 'urgent and important'),
        ('PLAN', 'not urgent but important'),
        ('DELEGATE', 'not important but urgent'),
        ('LIMIT', 'not urgent not important'),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    files = models.FileField(upload_to='documents/', null=True, blank=True)
    links = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(choices=PRIORITY, default='LIMIT')
    related_task = models.ManyToManyField('self', blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_task')
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField('Category', through='TaskCategory')


class Status(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_status')

    class Meta:
        unique_together = ('name', 'user')
        verbose_name = 'Status'


class Category(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_category')

    class Meta:
        unique_together = ('name', 'user')
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class TaskCategory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
