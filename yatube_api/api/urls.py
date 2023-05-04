from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, GroupViewSet, LightFollowViewSet,
                    PostViewSet)

app_name = 'api/jwt'

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(r'follow', LightFollowViewSet, basename='follower')
router_v1.register('posts/(?P<post_id>\\d+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
