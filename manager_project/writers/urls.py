from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:author_id>/', views.detail, name='auther'),
]
