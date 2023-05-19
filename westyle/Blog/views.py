from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import CommentForm, PostForm,EditForm
from .models import Comment, Post
from django.contrib import messages


class Blog(ListView):
    model =Post
    template_name ="blog.html"
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

class Addcomment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html" 
    success_url = reverse_lazy('Blog')
    # fields = '__all__'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
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
    