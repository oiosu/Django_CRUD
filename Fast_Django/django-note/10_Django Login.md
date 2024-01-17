### 10_Django Login

---

* ##### forms.py

> 사용자들로부터 데이터를 수집하고 유효성을 검사하는데 사용되는 장고 form을 정의하는 곳 
>
> 장고의 form 프레임워크를 활용하여 사용자 입력을 처리하고 저장하는데 도움이 된다. 
>
> `forms.py` 에서 정의된 form class들은 사용자 인터페이스에서 데이터를 수집하고 서버로 전송할 수 있는 HTML form을 생성하는 역할을 한다.

---





##### 1. 회원가입 

> **(1) forms.py ===> (2) urls.py ===> (3) views.py ===> (4) templates**

##### 1-(1) forms.py 

```python
from django import forms
from shortener.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):   
    full_name = forms.CharField(max_length=30, required=False, help_text="Optional.", label="이름")
    username = forms.CharField(max_length=30, required=False, help_text="Optional.", label="유저명")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.", label="이메일")

    class Meta:
        model = User
        fields = (
            "username",
            "full_name",
            "email",
            "password1",
            "password2",
        )
        
```



##### 1-(2) urls.py

```python
urlpatterns = [
    #...
    path("register", register, name="register"),
	#...
]
```



##### 1-(3) views.py

```python
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입완료"
        return render(request, "register.html", {"form": form, "msg": msg})
    else:
        return render(request, "register.html", {})
```



##### 2. 로그인

> **(1) forms.py ===> (2) urls.py ===> (3) views.py ===> (4) templates**



##### 2-(1) forms.py 

```python
from django import forms
from shortener.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "이메일"})
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "패스워드"}),
    )
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input", "id": "_loginRememberMe"}),
        required=False,
        disabled=False,
    )
```



##### 2-(2) urls.py

```python
urlpatterns = [
    #...
    path("login", login_view, name="login"),
    #...
]

```



##### 2-(3) views.py

```python
def login_view(request):
    is_ok = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            msg = "올바른 유저ID와 패스워드를 입력하세요."
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                pass
            else:
                if user.user.check_password(raw_password):
                    msg = None
                    login(request, user.user)
                    is_ok = True
                    request.session["remember_me"] = remember_me
                    return redirect("base")

    else:
        msg = None
        form = LoginForm()
        if request.user.is_authenticated:
            return redirect("index")
    return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})
```



##### 3. 로그아웃

##### 3-(1) urls.py

```python
urlpatterns = [
    #...
    path("logout", logout_view, name="logout"),
    #...
]
```



##### 3-(2) views.py

```python
def logout_view(request):
    logout(request)
    return redirect("login")
```

