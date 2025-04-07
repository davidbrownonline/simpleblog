from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
   path('', PostListView.as_view() , name='home'),
   path('post_detail/<int:pk>', PostDetailView.as_view(), name = 'post-detail'),
   path('post_create/', PostCreateView.as_view(), name = 'post-create'),
   path('post_edit/<int:pk>', PostUpdateView.as_view(), name = 'post-update'),
]