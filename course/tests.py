from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from course.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='user@test.com', password='test', group='user')
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            title='test',
            description='test',
            video_url='http://youtube.com',
            owner=self.user,
        )

    def test_create_lesson(self):
        """ Тестирование создание урока """
        data = {
            "title": 'test',
            'description': 'test',
            "video_url": "http://youtube.com"
        }
        response = self.client.post(
            reverse('course:lesson_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 2, 'title': 'test', 'preview': None, 'description': 'test', 'video_url': 'http://youtube.com',
             'course': None, 'owner': 1}
        )

    def test_destroy_list(self):
        response = self.client.delete(
            reverse('course:lesson_delete', kwargs={'pk': 3})
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_detail_list(self):
        response = self.client.get(
            reverse('course:lesson_get', kwargs={'pk': 4})
        )

        self.assertEquals(
            response.json(),
            {'id': 4, 'title': 'test', 'preview': None, 'description': 'test', 'video_url': 'http://youtube.com',
             'course': None, 'owner': 3}
        )

    def test_list_lesson(self):
        response = self.client.get(
            reverse('course:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 5, 'title': 'test', 'preview': None, 'description': 'test', 'video_url': 'http://youtube.com',
                 'course': None, 'owner': 4}]}

        )

    def test_update_list(self):
        response = self.client.put(
            reverse('course:lesson_update', kwargs={'pk': 6}),
            {"title": 'new_test',
             "description": 'new_test',
             'video_url': 'http://youtube.com'}
        )
        self.assertEquals(
            response.json(),
            {'id': 6, 'title': 'new_test', 'preview': None, 'description': 'new_test',
             'video_url': 'http://youtube.com', 'course': None, 'owner': 5}

        )
