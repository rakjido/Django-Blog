import logging

from django.http import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Board

logger = logging.getLogger('blog')


def board_list(request):
    """
    Board List
    """
    logger.info("board_list")
    board_list = Board.objects.order_by("-create_date")

    # 페이지당 표시 포스트 수
    post_num_per_page = 8
    # 페이지 수
    page_num = 5

    paginator = Paginator(board_list, post_num_per_page)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    page_min = int((posts.number - 1) / page_num) * page_num + 1
    page_max = min((page_min + page_num), paginator.num_pages + 1)
    page_range = range(page_min, page_max)
    return render(request, "board/list.html", {"board_list": posts, "page_range": page_range})


@login_required(login_url="/account/login")
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


@login_required(login_url="/account/login")
def board_put(request, pk):
    """
    Board Update
    """
    logger.info("board_put")
    post = get_object_or_404(Board, idx=pk)
    if request.user != post.author:
        messages.error(request, "You are not authorized")
        return redirect("/{}".format(post.idx))

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.update_date = timezone.now()
        post.save()
        return redirect("/")
    else:

        return render(request, "board/update.html", {"post": post})


@login_required(login_url="/account/login")
def board_delete(request, pk):
    """
    Board Delete
    """
    logger.info("board_delete")
    post = get_object_or_404(Board, idx=pk)
    if request.user != post.author:
        messages.error(request, "You are not authorized")
        return redirect("/{}".format(post.idx))

    post.delete()
    return redirect("board_list")
