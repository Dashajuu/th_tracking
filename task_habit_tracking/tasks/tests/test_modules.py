from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

from tasks.models import Task, Category, Status


class TaskModelTest(TestCase):
    databases = {'test'}

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.status = Status.objects.create(name='active')
        self.category1 = Category.objects.create(name='Work')
        self.category2 = Category.objects.create(name='Career', user=self.user)

        self.test_file = SimpleUploadedFile(
            name='test_file.txt',
            content=b'This is a test file.',
            content_type='text/plain'
        )

        self.task = Task.objects.create(
            name='Task 1',
            description='Description Task 1',
            files=self.test_file,
            links='https://pinterest.com/',
            deadline='2025-01-29 13:50',
            priority='DO',
            user=self.user,
            status=self.status
        )

        self.task.category.add(self.category1, self.category2)

    def test_task_creation(self):
        self.assertEqual(self.task.name, 'Task 1')
        self.assertEqual(self.task.description, 'Description Task 1')

        self.assertEqual(self.task.files, 'documents/test_file.txt')

        self.assertEqual(self.task.links, 'https://pinterest.com/')
        self.assertEqual(self.task.deadline, '2025-01-28 13:50')
        self.assertEqual(self.task.priority, 'DO')
        self.assertEqual(self.task.user.username, 'testuser')
        self.assertEqual(self.task.status, 'active')
