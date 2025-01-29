from django.test import TestCase
from django.contrib.auth.models import User

from habits.models import Habit
from tasks.models import Category


class HabitModelTest(TestCase):
    databases = {'test'}

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category1 = Category.objects.create(name='Health')
        self.category2 = Category.objects.create(name='Sport')

        self.habit = Habit.objects.create(
            name='Run',
            description='Run run run',
            deadline='2025-01-31 13:50',
            status='F',
            user=self.user
        )

        self.habit.category.add(self.category1, self.category2)

    def test_habit_creation(self):
        self.assertEqual(self.habit.name, 'Run')
        self.assertEqual(self.habit.description, 'Run run run')
        self.assertEqual(self.habit.deadline, '2025-01-31 13:50')
        self.assertEqual(self.habit.status, 'F')

        self.assertIn(self.category1, self.habit.category.all())
        self.assertIn(self.category2, self.habit.category.all())

    def test_remove_categories(self):
        self.habit.category.remove(self.category2)
        self.assertEqual(self.habit.category.count(), 1)
        self.assertIn(self.category1, self.habit.category.all())
