from django.urls import path
from . import api

# config path('api/posts/', include('post.urls')),
urlpatterns = [
    path('', api.ProductListView.as_view(), name='product_list'),
    path('feed/', api.PostListView.as_view(), name='post_list'),
    path('profile/<uuid:id>/', api.post_list_profile, name='post_list_profile'),
    path('<uuid:pk>/', api.post_detail, name='post_detail'),
    
    path('create/', api.post_create, name='post_create'),
    path('update/<uuid:pk>/', api.post_update, name='post_update'),
    path('<uuid:pk>/delete/', api.post_delete, name='post_delete'),
    
    path('create/product/', api.create_product, name='create_product'),
    path('create/review/', api.create_review, name='create_review'),
    
    path('<uuid:pk>/like/', api.post_like, name='post_like'),
    path('<uuid:pk>/likestatus/', api.check_liked, name='check_liked'),
    path('<uuid:pk>/comment/', api.post_create_comment, name='post_create_comment'),
    
    path('trends/', api.get_trends, name='get_trends'),
    
]

