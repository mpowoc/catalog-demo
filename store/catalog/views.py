import json
import boto3

from django.contrib.auth.models import Group, User
from store.catalog.models import CatalogItem
from rest_framework import permissions, viewsets

from store.catalog.serializers import CatalogItemSerializer, GroupSerializer, UserSerializer


# TODO - extract AWS config to configuration file
session = boto3.Session(
    aws_access_key_id='dummy', # replace with your key
    aws_secret_access_key='dummy', # replace with your key
)
sqs = session.resource('sqs',  endpoint_url='http://localhost:4566', region_name='us-east-1') # replace with your region name

class CatalogItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows catalog items to be viewed or edited.
    """
    queryset = CatalogItem.objects.all().order_by('-created')
    serializer_class = CatalogItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
        
        # Side effect: Publish creation event to SQS
        queue = sqs.get_queue_by_name(QueueName="catalog-events-queue")
        queue.send_message(
            MessageBody=json.dumps(serializer.data),
        )


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