from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostDeleteView, PostUpdateView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/new/', PostCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/detail', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete')
]