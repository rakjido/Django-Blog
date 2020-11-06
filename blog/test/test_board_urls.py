from django.test import SimpleTestCase
from django.urls import reverse, resolve

from board.views import board_list, board_post, board_get, board_put, board_delete


class TestBoardUrls(SimpleTestCase):
    def test_board_list_url(self):
        url = reverse("board_list")
        print(resolve(url))
        self.assertEquals(resolve(url).func, board_list)

    def test_board_list_url(self):
        url = reverse("board_get", args=[3])
        self.assertEquals(resolve(url).func, board_get)

    def test_board_list_url(self):
        url = reverse("board_post")
        self.assertEquals(resolve(url).func, board_post)

    def test_board_list_url(self):
        url = reverse("board_put", args=[4])
        self.assertEquals(resolve(url).func, board_put)

    def test_board_list_url(self):
        url = reverse("board_delete", args=[1000])
        self.assertEquals(resolve(url).func, board_delete)
