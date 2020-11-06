from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from board.models import Board


class BoardTestViews(TestCase):

    # def test_board_list_get(self):
    #     client = Client()
    #     response = client.get(reverse("board_list"))
    #     print(response)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "board/list.html")

    # 전체 테스트 실행 전 @classmethod가 없을 경우 각 테스트 실행 전
    @classmethod
    def setUp(self):
        self.client = Client()
        self.list_url = reverse("board_list")
        self.post_url = reverse("board_post")
        self.get_url = reverse("board_get", args=[1])
        self.put_url = reverse("board_put", args=[1])
        self.user = User.objects.create_user("testuser", "testuser@gmail.com", "1234")
        number_of_post = 10
        for post_id in range(number_of_post):
            Board.objects.create(
                title=f"test {post_id}", content=f"This is test #{post_id}", author=self.user
            )

    def test_board_list_GET(self):
        response = self.client.get(self.list_url)
        # print(response.context)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "board/list.html")

    def test_board_post_GET(self):
        # @login_required 가 있을 경우
        self.client.login(username="testuser", password="1234")
        response = self.client.get(self.post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "board/new.html")
        self.assertEqual(str(response.context["user"]), "testuser")

    def test_board_post_POST(self):
        self.client.login(username="testuser", password="1234")
        response = self.client.post(
            self.post_url, {"title": "test", "content": "test content", "author": self.user}
        )
        # HTTP 302 : redirect
        # self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_board_post_POST_no_data(self):
        self.client.login(username="testuser", password="1234")
        ## error
        response = self.client.post(self.post_url)
        self.assertRedirects(response, "/")

    def test_board_get_GET(self):
        response = self.client.get(self.get_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "board/view.html")
        self.assertEquals(response.context["post"].title, "test 0")
        self.assertEquals(response.context["post"].content, "This is test #0")

    def test_board_put_GET(self):
        self.client.login(username="testuser", password="1234")
        response = self.client.get(self.put_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "board/update.html")
        self.assertEqual(str(response.context["user"]), "testuser")

    # def test_board_put_POST(self):
    #     self.client.login(username="testuser", password="1234")
    #     response = self.client.post(
    #         self.post_url, {"title": "updated title", "content": "updated content ", "author": self.user}
    #     )
    #     self.assertRedirects(response, "/")