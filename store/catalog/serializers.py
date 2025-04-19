from django.contrib.auth.models import Group, User
from store.catalog.models import CatalogItem
from rest_framework import serializers

class CatalogItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogItem
        fields = ['created', 'title', 'description']
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']