from django.urls import path
from . import views

app_name='pirostagram'

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('create', views.post_create, name="post_create"),
    path('<int:pk>', views.post_detail, name="post_detail"),
    path('<int:pk>/update', views.post_update, name="post_update"),
    path('<int:pk>/delete', views.post_delete, name="post_delete"),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('comment_ajax/', views.comment_ajax, name='comment_ajax'),
    path('comment_delete_ajax/', views.comment_delete_ajax, name='comment_delete_ajax')
]