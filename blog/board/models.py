from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Board(models.Model):
    """
    Blog Board Model
    """

    idx = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-create_date",)

    def get_absolute_url(self):
        return reverse("board_get", kwargs={"pk": self.idx})

    def __str__(self):
        return self.title