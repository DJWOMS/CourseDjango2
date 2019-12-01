from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Класс формы комментариев"""
    class Meta:
        model = Comment
        fields = ("text", )
