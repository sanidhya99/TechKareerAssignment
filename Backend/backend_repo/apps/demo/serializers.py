# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework import serializers
from .models import Post, Comment
from random import sample
from django.db.models import Count

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'user']

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'user', 'comment_count', 'comments']

    def get_comments(self, obj):
        queryset = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(queryset, many=True).data
    
'''

FOLLOW-UP Q 
    def get_comments(self, obj):
        all_comments = list(obj.comments.all())
        random_comments = sample(all_comments, min(len(all_comments), 3))
        return CommentSerializer(random_comments, many=True).data
        
'''