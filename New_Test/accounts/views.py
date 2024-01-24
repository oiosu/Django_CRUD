from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm

def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {"user": user}
    return render(request, "accounts/detail.html", context)

@login_required
def follow(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        messages.warning(request, "스스로 팔로우 할 수 없습니다.")
        return redirect("accounts:detail", pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect("accounts:detail", pk)

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # 백엔드 지정
            user.save()
            auth_login(request, user)
            return redirect("main")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("main")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)

def logout_view(request):
    auth_logout(request)
    messages.warning(request, "로그아웃 성공!")
    return redirect("main")

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)

