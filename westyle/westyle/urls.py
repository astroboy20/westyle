"""westyle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include 
from Logic.views import Home
from Blog.views import Blog, ArticleDetail,Addpost,Updatepost,Deletepost,Addcomment
from Users.views import UserRegistration
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="Home"),
    path('blog', Blog.as_view(), name="Blog"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article_detail"),
    path('addPost', Addpost.as_view(), name="Add_Post"),
    path('article/edit/<int:pk>', Updatepost.as_view(), name="update_post"),
    path('article/edit/<int:pk>/delete', Deletepost.as_view(), name="delete_post"),
    path('article/<int:pk>/comment',Addcomment.as_view(),name= 'add_comment' ),
    path('members/', include('django.contrib.auth.urls')),
    path('register/',UserRegistration.as_view(), name='register' ),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
