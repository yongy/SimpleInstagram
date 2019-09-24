from django.urls import path
from Insta.views import (HellowWorld, PostsView, PostDetailView, PostCreateView, 
                         PostDeleteView, PostUpdateView)

urlpatterns = [
    path('', HellowWorld.as_view(), name = 'helloworld'),
    path('posts/', PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', PostCreateView.as_view(), name = 'create_post'),    
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name = 'update_post'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name = 'delete_post')
]