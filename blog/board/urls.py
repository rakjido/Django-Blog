from django.urls import path

from . import views

urlpatterns = [
    path("", views.board_list, name="board_list"),
    path("<int:pk>/", views.board_get, name="board_get"),
    path("new/", views.board_post, name="board_post"),
    path("<int:pk>/update", views.board_put, name="board_put"),
    path("<int:pk>/delete", views.board_delete, name="board_delete"),
]
