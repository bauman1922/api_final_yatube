from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, GroupViewSet, LightFollowViewSet,
                    PostViewSet)

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'follow', LightFollowViewSet, basename='follower')
router.register('posts/(?P<post_id>\\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
