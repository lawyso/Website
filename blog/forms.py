__author__ = 'Emmah'
from django import forms

from .models import Post,Comment

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields =['comment']