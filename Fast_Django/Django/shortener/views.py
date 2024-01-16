from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .forms import RegisterForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


def index(request):
    user = User.objects.filter(id=request.user.id).first()
    email = user.email if user else "Anonymous User!"
    print("Logged in?", request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User!"
    print()
    return render(request, "base.html", {"welcome_msg": f"hello {email}", "hello": "world"})

@csrf_exempt
# user_id는 urls.py에서 가져오는 값이다.
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

# 회원가입
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."
        if form.is_valid():
            form.save()
            username = form.cleaned_date.get("username")
            raw_password = form.cleaned_date.get("password")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입완료"
        return render(request, "register.html", {"form": form, "msg": msg})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    

# 로그인
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)  
        msg = "가입되어 있지 않거나 로그인 정보가 잘못되었습니다"
        print(form.is_valid)  
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None: 
                msg = "로그인 성공"
                login(request, user)
        return render(request, "login.html", {"form": form, "msg": msg})
    else:
        form = AuthenticationForm()  
        return render(request, "login.html", {"form": form})

# 로그아웃
def logout_view(request):
    logout(request)  
    return redirect("index")