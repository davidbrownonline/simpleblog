
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
    path('', PostListView.as_view(), name = 'post-list'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name = 'post-detail'),
    path('post_create/', PostCreateView.as_view(), name = 'post-create'),
    path('post_update/<int:pk>', PostUpdateView.as_view(), name = 'post-update'),
]