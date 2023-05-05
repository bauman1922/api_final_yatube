from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import (CommentViewSet, GroupViewSet, LightFollowViewSet,
                    PostViewSet)

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(r'follow', LightFollowViewSet, basename='follower')
router_v1.register('posts/(?P<post_id>\\d+)/comments',
                   CommentViewSet, basename='comments')

jwt_patterns = [
    path(
        'create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'verify/',
        TokenVerifyView.as_view(),
        name='token_verify'),
]

urlpatterns = [
    path('v1/jwt/', include(jwt_patterns)),
    path('v1/', include(router_v1.urls)),
]
