from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from . import serializers, models, permissions
from django.shortcuts import render, get_object_or_404


class PostListView(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    permission_classes = [IsAuthorOrReadOnly]


class LikeCreateView(generics.CreateAPIView):
    queryset = models.Like.objects.all()
    serializer_class = serializers.LikeSerializer


class LikeDeleteView(generics.DestroyAPIView):
    queryset = models.Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = [permissions.IsAuthorOrReadOnly]


class CommentCreateView(generics.CreateAPIView):
    queryset = models.Comments.objects.all()
    serializer_class = serializers.CommentSerializer

