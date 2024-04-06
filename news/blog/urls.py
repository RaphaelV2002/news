# blog/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news_table/", views.news_table, name="news_table"),
    path("login/", views.views.LoginView.as_view(), name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.log_out, name="logout"),
    path("blog/<int:blog_id>/", views.blog, name="blog"),
    path("blogs/", views.blogs, name="blogs"),
    path("blog/<int:blog_id>/delete/", views.delete_blog, name="delete_blog"),
    path("blog/<int:blog_id>/create_new/", views.create_new, name="create_new"),
    path(
        "blog/<int:new_id>/delete_new/",
        views.delete_new,
        name="delete_new",
    ),
    path("blog/<int:new_id>/update/", views.update_new, name="update_new"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
