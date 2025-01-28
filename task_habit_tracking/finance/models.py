from django.db import models
from django.contrib.auth.models import User


class Finance(models.Model):
    FINANCE_TYPE = [
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('savings', 'Savings'),
    ]

    type = models.CharField(max_length=20, choices=FINANCE_TYPE)
    note = models.TextField(max_length=350, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    is_recurring = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', through='FinanceCategory')


class Category(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='finance_category_user')

    class Meta:
        unique_together = ('name', 'user')
        verbose_name = 'Finance category'


class FinanceCategory(models.Model):
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
