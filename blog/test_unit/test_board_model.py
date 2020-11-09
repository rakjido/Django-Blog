from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from board.models import Board


class BoardTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("testuser", "testuser@gmail.com", "1234")
        self.board = Board.objects.create(title="TestCase", content="This is TestCase", author=self.user)

    def test_board(self):
        self.assertEqual(self.board.title, "TestCase")
        self.assertEqual(self.board.author.username, "testuser")

    def test_board_get_abolute_url(self):
        self.assertEquals(self.board.get_absolute_url(),'/1/')