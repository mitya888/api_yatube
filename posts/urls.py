from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet, basename='all-posts')
router.register(r'api/v1/posts/(?P<id>[0-9]+)/comments',
                CommentViewSet,
                basename='all-post')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
