from django.contrib.auth.models import Group, User
from store.catalog.models import CatalogItem
from rest_framework import permissions, viewsets

from store.catalog.serializers import CatalogItemSerializer, GroupSerializer, UserSerializer

class CatalogItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows catalog items to be viewed or edited.
    """
    queryset = CatalogItem.objects.all().order_by('-created')
    serializer_class = CatalogItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]