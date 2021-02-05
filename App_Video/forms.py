from django import forms
from . import models

class CommentForm(forms.ModelForm):
    comment=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Enter Your Comment'}))
    class Meta:
        model=models.Comments
        fields=('comment',)
        
