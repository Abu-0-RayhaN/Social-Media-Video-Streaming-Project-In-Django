from django import forms
from .models import Posts,Comment

class PostForm(forms.ModelForm):
    caption = forms.CharField(
        required = False,
        label = "Caption:"
    )
    class Meta:
        model = Posts
        fields =('image','caption')

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields =['comment']