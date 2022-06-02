from dataclasses import fields
from pyexpat import model
from statistics import mode
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,EditForm
from .models import Post
from django.contrib import messages
# Create your views here.
# def Blog(request):
#     return render(request, "blog.html")

class Blog(ListView):
    model =Post
    template_name ="blog.html"
    # ordering = ['-id']
    ordering = ['-post_date']
    ordering = ['-id']
    
class ArticleDetail(DetailView):
    model =Post
    template_name = 'blog_details.html'
    
class Addpost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html" 
    # fields = '__all__'
    
class Updatepost(UpdateView):
    model = Post 
    template_name = 'update_blog.html'
    # fields = ['title', 'body']
    form_class = EditForm
    
    
class Deletepost(DeleteView):
    model = Post 
    template_name = 'Delete_post.html'
    success_url = reverse_lazy('Blog')
    # messages.success(request,'Post deleted successfully!')
    