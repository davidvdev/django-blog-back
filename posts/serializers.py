from .models import Post
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title","body"]