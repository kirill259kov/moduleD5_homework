from django.forms import ModelForm
from .models import Post
from django import forms
from django.contrib.auth.models import Group
from django.db import models


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text']