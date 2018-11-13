from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('', views.post_list, name='post_list'),
    path('<int:author_id>/', views.detail, name='auther'),
]
