from django.urls import include, path
from rest_framework import routers

from store.catalog import views as catalogViews

router = routers.DefaultRouter()
router.register(r'catalogitems', catalogViews.CatalogItemViewSet)
router.register(r'users', catalogViews.UserViewSet)
router.register(r'groups', catalogViews.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("search/", include("store.search.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]