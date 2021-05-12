from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='post')
router.register(r'v1/posts/(?P<id>[0-9]+)/comments',
                CommentViewSet,
                basename='comment')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
