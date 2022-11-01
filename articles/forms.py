from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "grade", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "",
                    "style": "height: 50px; resize: none; width: 100%;",
                }
            ),
        }
        labels = {
            "content": "댓글",
        }
