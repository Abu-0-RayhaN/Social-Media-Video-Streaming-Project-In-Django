from django import forms
from .models import Uploads,Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields =['comment']
class VideoForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields =['title','category','thambnail','videofile']
        