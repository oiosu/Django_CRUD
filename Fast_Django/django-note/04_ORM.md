### 04. ORM

`https://docs.djnagoproject.com/en/3.2/topics/db/queries/`

> `.get()` , `.all()`, `.filter()`, `.save()`, `.delete()`, `.update()`, `.exists()`, `.first()`, `.count()`, 
> `.select_related()`, `.prefetch_related()`, `.order_by()`



* ##### Django Debug Toolbar

`https://django-debug-toolbar.readthedocs.io/en/latest/index.html`

> SQL, TIME, Cache

◾ Step(1) install

```bash
python -m pip install django-debug-toolbar
```

◾Step(2) settings.py

```python
INSTALLED_APPS = [
    #....
    'debug_toolbar'
]
```

```python
MIDDLEWARE = [
     #....
    "debug_toolbar.middleware.DebutToolbarMiddleware",
]
```

![image-20240116093944701](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116093944701.png)



* requirements

```bash
pip install -r requirements.txt
```



* pip upgrade

```bash
pip install -r requirements.txt
```



