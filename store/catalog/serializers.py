import json
import boto3

from django.contrib.auth.models import Group, User
from store.catalog.models import CatalogItem
from rest_framework import serializers

# TODO - extract AWS config to configuration file
session = boto3.Session(
    aws_access_key_id='dummy', # replace with your key
    aws_secret_access_key='dummy', # replace with your key
)
sqs = session.resource('sqs', region_name='us-east-1') # replace with your region name

class CatalogItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogItem
        fields = ['created', 'title', 'description']

    def create(self, validated_data):
        # Create the item
        item = CatalogItem.objects.create(**validated_data)

        # Side effect: Publish creation event to SQS 
        queue = sqs.get_queue_by_name(QueueName="catalog-events-queue")
        response = queue.send_message(
            MessageBody=json.dumps(item),
        )

        return item

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']