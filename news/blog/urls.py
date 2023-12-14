# blog/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.views.LoginView.as_view(), name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.log_out, name="logout"),
    path("blog/<int:blog_id>/", views.blog, name="blog"),
    path("blogs/", views.blogs, name="blogs"),
    path("blog/<int:blog_id>/delete/", views.delete_blog, name="delete_blog"),
    path("blog/delete_new/<int:new_id>/", views.delete_new, name="delete_new"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
