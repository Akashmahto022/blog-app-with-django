from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('all-blog/', views.blog_list, name = 'blog_list'),
    path('blog-create/', views.blog_create, name = 'blog_create'),
    path('<int:blog_id>/blog-edit/', views.blog_edit, name = 'blog_edit'),
    path('<int:blog_id>/blog-delete-confirmation', views.blog_delete, name = 'blog_delete'),
]