# import json
# import boto3

from django.contrib.auth.models import Group, User
from store.catalog.models import CatalogItem
from rest_framework import serializers

# session = boto3.Session(
#     aws_access_key_id='<AWS_ACCESS_KEY_ID>', # replace with your key
#     aws_secret_access_key='<AWS_SECRET_ACCESS_KEY>', # replace with your key
# )
# sqs = session.resource('sqs', region_name='<AWS_REGION_NAME>') # replace with your region name

class CatalogItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogItem
        fields = ['created', 'title', 'description']

    # def create(self, validated_data):
    #     # Create the item
    #     item = CatalogItem.objects.create(**validated_data)

    #     # Side effect: Publish creation event to SQS 
    #     queue = sqs.get_queue_by_name(QueueName="catalog-events")
    #     response = queue.send_message(
    #         MessageBody=json.dumps(item),
    #         MessageGroupId='messageGroupId'
    #     )

    #     return item

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']