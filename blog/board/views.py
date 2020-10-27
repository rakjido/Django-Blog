import logging

from django.http import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Board

logger = logging.getLogger(__name__)


def board_list(request):
    """
    Board List
    """
    logger.info("board_list")
    board_list = Board.objects.order_by("-create_date")
    # 페이지당 표시 포스트 수
    paginator = Paginator(board_list, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "board/list.html", {"page": page, "board_list": posts})


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


def board_put(request, pk):
    """
    Board Update
    """
    logger.info("board_put")
    if request.method == "POST":
        post = get_object_or_404(Board, idx=pk)
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        user = get_object_or_404(User, username=request.POST.get("author"))
        post.author = user
        post.update_date = timezone.now()
        post.save()
        return redirect("/")
    else:
        post = get_object_or_404(Board, idx=pk)
        return render(request, "board/update.html", {"post": post})


def board_delete(request, pk):
    """
    Board Delete
    """
    logger.info("board_delete")
    post = get_object_or_404(Board, idx=pk)
    post.delete()
    return redirect("board_list")
