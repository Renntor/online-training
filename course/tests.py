from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='user@test.com', password='test', group='user')
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """ Тестирование создание урока """
        data = {
            "title": 'test',
            'description': 'test',
            "video_url": "http://youtube.com"
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
