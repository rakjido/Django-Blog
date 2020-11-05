from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from board.models import Board


class BoardTestCase(TestCase):
    def setUp(self):
        user = get_object_or_404(User, username="admin")
        Board.objects.create(title="TestCase", content="This is TestCase", author=user)

    def test_board(self):
        user = get_object_or_404(User, username="admin")
        test = Board.objects.get(title="TestCase")
        self.assertEqual(test.content, "This is TestCase")
        self.assertEqual(test.author, user)
