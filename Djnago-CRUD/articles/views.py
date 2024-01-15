from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
    }

    return render(request, "movie/index.html", context)


def new(request):
    return render(request, "movie/new1.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Review.objects.create(title=title, content=content)
    context = {
        "title": title,
        "content": content,
    }

    return redirect("movie:index")


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    context = {
        "review": review,
    }

    return render(request, "movie/detail.html", context)


def edit(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    context = {
        "review": review,
    }

    return render(request, "movie/edit.html", context)


def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    review.title = request.GET.get("title")
    review.content = request.GET.get("content")

    review.save()

    return redirect("movie:index")


def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    review.delete()

    return redirect("movie:index")