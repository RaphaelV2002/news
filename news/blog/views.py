# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import views, login, logout
from . import models
from . import forms


def home(request, *args, **kwargs):
    """Загружает главную страницу с пятью последними новостями, отсортированным по времени публикации."""
    news = models.New.objects.new()[:5]
    return render(
        request,
        "home.html",
        {
            "news": news,
        },
    )


def blogs(request, *args, **kwargs):
    """Загружает страницу со всеми блогами и формой для создания нового блога."""
    blogs = models.Blog.objects.new()
    if request.method == "POST":
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return HttpResponseRedirect(reverse("blog", kwargs={"blog_id": blog.id}))
    else:
        form = forms.BlogForm()
    return render(
        request,
        "blogs.html",
        {
            "form": form,
            "blogs": blogs,
        },
    )


def blog(request, *args, **kwargs):
    """Загружает страницу блога с новостями из этого блога и формой для создания новости."""
    blog = get_object_or_404(models.Blog, pk=kwargs["blog_id"])
    news = blog.new.all()
    if request.method == "POST":
        form = forms.NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.blog = blog
            new.author = request.user
            new.save()
            return HttpResponseRedirect(reverse("blog", kwargs={"blog_id": blog.id}))
    else:
        form = forms.NewForm()
    return render(request, "blog.html", {"form": form, "news": news, "blog": blog})


def delete_blog(request, *args, **kwargs):
    """Удаляет блог и направляет на страницу блогов."""
    models.Blog.objects.filter(pk=kwargs["blog_id"], author=request.user).delete()
    return HttpResponseRedirect("/blogs/")


def delete_new(request, *args, **kwargs):
    """Удаляет новость и направляет на текущую страницу."""
    models.New.objects.filter(pk=kwargs["new_id"], author=request.user).delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def signup(request, *args, **kwargs):
    """Загружает страницу с формой для регистрации нового пользователя."""
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("login"))
    else:
        form = forms.SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


def log_out(request, *args, **kwargs):
    """Выход пользователя."""
    logout(request)
    return HttpResponseRedirect("/")
