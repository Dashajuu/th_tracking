from django.test import TestCase
from django.contrib.auth.models import User

from finance.models import Finance, Category


class FinanceModelTest(TestCase):
    databases = {'test'}

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category1 = Category.objects.create(name='Salary')
        self.category2 = Category.objects.create(name='Travel')

        self.finance = Finance.objects.create(
            type='savings',
            note='savings 50',
            amount=234.8,
            is_recurring=True,
            due_date='2023-02-01 13:50',
            user=self.user
        )

        self.finance.category.add(self.category1, self.category2)

    def test_habit_creation(self):
        self.assertEqual(self.finance.type, 'savings')
        self.assertEqual(self.finance.note, 'savings 50')
        self.assertEqual(self.finance.amount, 234.8)
        self.assertEqual(self.finance.is_recurring, True)
        self.assertEqual(self.finance.due_date, '2023-02-01 13:50')

        self.assertIn(self.category1, self.finance.category.all())
        self.assertIn(self.category2, self.finance.category.all())

    def test_remove_categories(self):
        self.finance.category.remove(self.category2)
        self.assertEqual(self.finance.category.count(), 1)
        self.assertIn(self.category1, self.finance.category.all())



