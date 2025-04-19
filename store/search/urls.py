from django.urls import path

from .views import SearchCatalogItems

urlpatterns = [
    path("catalogitems/<str:query>/", SearchCatalogItems.as_view()),
]