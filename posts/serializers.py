from rest_framework import serializers
from . import models
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'body', 'date', 'author', 'video', 'image')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = ('post', 'user', 'is_like')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = ('post', 'user', 'active', 'created','text')


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Post
        fields = ('id', 'title', 'body', 'date', 'author', 'video', 'image', 'comments', 'likes')
