from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post


class CreatePost(forms.ModelForm):
    status = forms.IntegerField()

    class Meta:
        model = Post
        fields = ["title","slug","author", "content","status"]