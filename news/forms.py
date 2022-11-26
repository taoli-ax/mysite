from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {'content': forms.Textarea(attrs={'placeholder': '我来评两句~~'})}


class PunchIn(forms.Form):
    template_name = 'news/punch_in.html'
    express = forms.CharField(max_length=50, label='mood')
