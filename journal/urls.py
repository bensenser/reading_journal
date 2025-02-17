from django.urls import path
from . import views  # ✅ Импортируем views из текущего приложения
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),  # Главная страница (список книг)
    path("register/", views.register, name="register"),  # Регистрация

    # Вход через стандартный Django LoginView
    path("login/", auth_views.LoginView.as_view(
        template_name="journal/login.html",
        redirect_authenticated_user=True
    ), name="login"),

    # Выход через стандартный Django LogoutView
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    path("add_book/", views.add_book, name="add_book"),  # Добавление книги
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),  # Удаление книги
]
