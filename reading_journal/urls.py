from django.contrib import admin
from django.urls import include, path  # ✅ Используем include()

urlpatterns = [
    path("admin/", admin.site.urls),  # Стандартная админка Django
    path("", include("journal.urls")),  # Подключаем маршруты приложения journal
]
