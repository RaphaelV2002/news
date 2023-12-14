# blog/form.py
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from . import models


class BlogForm(ModelForm):
    class Meta:
        model = models.Blog
        fields = ["title"]


class NewForm(ModelForm):
    class Meta:
        model = models.New
        fields = ["title", "text", "image"]


class LoginForm(ModelForm):
    class Meta:
        model = models.User
        fields = ["username", "password"]


class SignUpForm(ModelForm):
    class Meta:
        model = models.User
        fields = ["username", "email", "password"]
        help_texts = {
            "username": None,
        }
