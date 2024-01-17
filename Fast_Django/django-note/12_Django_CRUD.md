### 12_Django_CRUD

> Create, Read, Update, Delete



#### Read, Delete

* ##### views.py

```python
def url_list(reqeust):
    get_list = ShortenedUrls.objects.order_by("-created_at").all()
    return render(request, "url_list.html", {"list": get_list})
```

* ##### models.py

```python
class ShortenedUrls(models.Model):
    class UrlCreatedVia(models.TextChoices):
        WEBSITE = "web"
        TELEGRAM = "telegram"
        
    def rend_string():
        str_pool = string.digits + string.ascii_letters
        return("".join([random.choice(str_pool) for _ in range(6)])).lower()
    
    nick_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Users, on_delte=models.CASCADE)
    target_url = models.CharField(max_lenght=2000)
    shortened_url = models.CharField(max_lenth=8, choice=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```bash
python manage.py makemigrations
python manage.py migrate
```



* ##### url_list.html

```django
{% extends 'base.html' %}
{% load static %}
{% block title%}URL 리스트{% endblock %}
{% block main_breadscumb%}대시보드{% endblock %}
{% block sub_breadscumb_highlight %}URL List{% endblock%}
{% block sub_breadscumb %}URL 리스트{% endblock %}
{% block content %}
```



#### Update, Create

* ##### urls.py

```python
path("create", url_create, name="url_create")
```

* ##### views.py

```python
@login_required
def url_create(request):
    msg = None
    if request.method == "POST":
        form = UrlCreateForm(request.POST)
        if form.is_valid():
            msg = f"{form.cleaned_data.get('nick_name')} 생성 완료!"
            messages.add_message(request, messages.INFO, msg)
            form.save(request)
            return redirect("url_list")
        else:
            form = UrlCreateForm()
    else:
        form = UrlCreateForm()
    return render(request, "url_create.html", {"form": form})
```

* ##### forms.py

```python
class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrls
        fields = ["nick_name", "target_url"]
        labels = {
            "nick_name": _("별칭"),
            "target_url": _("URL"),
        }
        widgets = {
            "nick_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL을 구분하기 위한 별칭"}),
            "target_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "포워딩될 URL"}),
        }

    def save(self, request, commit=True, is_admin=False):
        instance = super(UrlCreateForm, self).save(commit=False)
        if not is_admin:
            instance.creator_id = request.users_id
        instance.target_url = instance.target_url.strip()
        if commit:
            try:
                instance.save()
            except Exception as e:
                print(e)
            else:
                url_count_changer(request, True)
        return instance

    def update_form(self, request, url_id, is_admin=False):
        instance = super(UrlCreateForm, self).save(commit=False)
        instance.target_url = instance.target_url.strip()
        ShortenedUrls.objects.filter(pk=url_id).update(target_url=instance.target_url, nick_name=instance.nick_name)

```

