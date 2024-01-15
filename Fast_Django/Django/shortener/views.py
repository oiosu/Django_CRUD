from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

def index(request):
    user = User.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User!"
    print(email)
    print(request.user.is_authenticated)
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
