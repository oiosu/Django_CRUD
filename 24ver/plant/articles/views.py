from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by("-pk")
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("articles:index")

    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context=context)


@login_required
def detail(request, pk):
    # 특정 글을 가져온다.
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            # POST : input 값 가져와서, 검증하고, DB에 저장
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                article_form.save()
                messages.success(request, "글이 수정되었습니다.")
                return redirect("articles:detail", article.pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
        else:
            # GET : Form을 제공
            article_form = ArticleForm(instance=article)
        context = {"article_form": article_form}
        return render(request, "articles/form.html", context)
    else:
        # 작성자가 아닐 때
        # (1) 403 에러메시지를 던져버린다.
        # from django.http import HttpResponseForbidden
        # return HttpResponseForbidden()
        # (2) flash message 활용!
        messages.warning(request, "작성자만 수정할 수 있습니다.")
        return redirect("articles:detail", article.pk)


@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect("articles:detail", article.pk)


@login_required
def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 만약 로그인한 유저(request.user)가 이 글을 좋아요 눌렀다면,
    if request.user in article.like_users.all():
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
        is_liked = False
    else:  # 좋아요 누르지 않은 상태라면 좋아요에 추가하고
        article.like_users.add(request.user)
        is_liked = True
        # 상세 페이지로 redirect
        context = {"isLiked": is_liked, "likeCount": article.like_users.count()}
    return redirect("articles:detail", article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("articles:index")
    context = {"article": article}
    return render(request, "articles/detail.html", context)

