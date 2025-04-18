from django.urls import path

from search.views import SearchCatalogItems

urlpatterns = [
    path("catalogitems/<str:query>/", SearchCatalogItems.as_view()),
]