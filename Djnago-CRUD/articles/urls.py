from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path("", views.index, name="index"),
    #  create
    path('new/', views.new, name='name'),
    path("create/", views.create, name="create"),
    # content
    path("detail/<int:review_pk>", views.detail, name="detail"),
    #  update
    path("edit/<int:review_pk>", views.edit, name="edit"),
    path("update/<int:review_pk>", views.update, name="update"),
    # delete
    path("delete/<int:review_pk>", views.delete, name="delete"),
    
]