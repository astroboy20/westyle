from django import forms 
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body','header_image')
        
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            # "author": forms.TextInput(attrs={'class':'form-control', 'placeholder':'User' , 'id':'user', 'value':'', 'type':'hidden'}),
            "author": forms.Select(attrs={'class':'form-control'}),
            "body": forms.Textarea(attrs={'class':'form-control'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            # "author": forms.Select(attrs={'class':'form-control'}),
            "body": forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "body": forms.Textarea(attrs={'class':'form-control'}),
        }

