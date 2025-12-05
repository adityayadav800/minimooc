from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Course, Lesson

User = get_user_model()

class MinimalTests(TestCase):
    def test_create_course_and_lesson(self):
        c = Course.objects.create(title='Demo', short_description='x', long_description='y')
        l = Lesson.objects.create(course=c, title='L1', content='content')
        self.assertEqual(c.lessons.count(), 1)
