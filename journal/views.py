from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import ReadBook, User
from .forms import RegistrationForm, ReadBookForm
from django.shortcuts import get_object_or_404, redirect
from .models import ReadBook




@login_required
def index(request):
    books = ReadBook.objects.filter(user=request.user)
    return render(request, "journal/index.html", {"books": books})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # ✅ Пароль уже хешируется автоматически
            login(request, user)
            return redirect("index")
    else:
        form = RegistrationForm()
    return render(request, "journal/register.html", {"form": form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")  # Если уже вошел, перенаправляем на главную
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "journal/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def add_book(request):
    if request.method == "POST":
        form = ReadBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect("index")
    else:
        form = ReadBookForm()
    return render(request, "journal/add_book.html", {"form": form})

def delete_book(request, book_id):
    book = get_object_or_404(ReadBook, id=book_id)
    book.delete()
    return redirect('index') 