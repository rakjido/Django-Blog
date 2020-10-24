import logging

from django.http import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Board

logger = logging.getLogger(__name__)


def board_list(request):
    """
    Board List
    """
    logger.info("board_list")
    board_list = Board.objects.order_by("-create_date")
    return render(request, "board/list.html", {"board_list": board_list})


def board_post(request):
    """
    Board Posting
    """
    logger.info("board_post")
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = get_object_or_404(User, username=request.POST.get("author"))
        Board.objects.create(title=title, content=content, author=user)
        return redirect("/")
    else:
        return render(request, "board/new.html", {})


def board_get(request, pk):
    """
    Board View
    """
    logger.info("board_get")
    post = get_object_or_404(Board, idx=pk)
    return render(request, "board/view.html", {"post": post})


# TO DO
def board_put(request, pk):
    """
    Board Update
    """
    logger.info("board_put")
    post = get_object_or_404(Board, idx=pk)
    post.title = request.POST.get("title")
    post.content = request.POST.get("content")
    post.author = request.POST.get("author")
    post.update_date = timezone.now()
    post.save()
    return redirect("/")


def board_delete(request, pk):
    """
    Board Delete
    """
    logger.info("board_delete")
    post = get_object_or_404(Board, idx=pk)
    post.delete()
    return redirect("board_list")
