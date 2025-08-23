from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["author", "created_at", "updated_at"]

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments =  CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id", "author", "title", "content",
            "created_at", "updated_at",
            "comments_count", "comments"
        ]
        read_only_fields = ["author", "created_at", "updated_at"]


        def validate_title(self, value):
            if len(value.strip()) < 3:

             raise serializers.ValidationError("Title must be at least 3 characters.")
        
            return value

    