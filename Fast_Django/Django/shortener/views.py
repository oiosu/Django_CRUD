from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .forms import RegisterForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    user = User.objects.filter(id=request.user.id).first()
    email = user.email if user else "Anonymous User!"
    print("Logged in?", request.user.is_authenticated)
    if not request.user.is_authenticated:
        email = "Anonymous User!"
    print()
    return render(request, "base.html", {"welcome_msg": f"hello {email}", "hello": "world"})

@csrf_exempt
def get_user(request, user_id):
    print(user_id)
    if request.method == "GET":
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = User.objects.filter(pk=user_id).first()
        return render(request, "base.html", {"user": user, "params": [abc, xyz]})
    elif request.method == "POST":
        username = request.POST.get("username")
        if username:
            user = User.objects.filter(pk=user_id).update(username=username)
            return JsonResponse({"msg": "you just reached with post method!"})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")  # 수정된 부분
            raw_password = form.cleaned_data.get("password")  # 수정된 부분
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입완료"
        return render(request, "register.html", {"form": form, "msg": msg})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

def login_view(request):
    msg = None
    is_ok = False
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                is_ok = True
        else:
            msg = "올바른 유저 ID와 패스워드를 입력하세요."
    else:
        form = AuthenticationForm()
    for visible in form.visible_fields():  # 수정된 부분
        visible.field.widget.attrs["placeholder"] = "유저ID" if visible.name == "username" else "패스워드"
        visible.field.widget.attrs["class"] = "form-control"
    return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})

def logout_view(request):
    logout(request)
    return redirect("index")

@login_required
def list_view(request):
    page = int(request.GET.get("p", 1))
    users = User.objects.all().order_by("-id")
    paginator = Paginator(users, 1)
    users = paginator.get_page(page)
    return render(request, "borders.html", {"users": users})
