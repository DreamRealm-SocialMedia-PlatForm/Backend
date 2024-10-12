from rest_framework import serializers
from .models import DreamCategory, Dream,  DreamComment



class DreamCategorySerializer(serializers.ModelSerializer):
        #--------------------------
    class Meta:
        model            = DreamCategory
        fields           = ['id', 'name']
        read_only_fields = ['id'] 



class DreamCommentSerializer(serializers.ModelSerializer):
    likes_count          = serializers.SerializerMethodField()
    dislikes_count       = serializers.SerializerMethodField()
    is_liked_by_user     = serializers.SerializerMethodField()
    is_disliked_by_user  = serializers.SerializerMethodField()

    class Meta:
        model  = DreamComment
        fields = ['id', 'comment', 'created_at', 'likes_count', 'dislikes_count', 'is_liked_by_user', 'is_disliked_by_user']

    def get_likes_count(self, obj):
        return obj.dream_comment_likes.count()

    def get_dislikes_count(self, obj):
        return obj.dream_comment_dislikes.count()

    def get_is_liked_by_user(self, obj):
        user = self.context.get('request').user
        return obj.dream_comment_likes.filter(user=user).exists()

    def get_is_disliked_by_user(self, obj):
        user = self.context.get('request').user
        return obj.dream_comment_dislikes.filter(user=user).exists()

class DreamSerializer(serializers.ModelSerializer):
    
    likes_count         = serializers.SerializerMethodField()
    dislikes_count      = serializers.SerializerMethodField()
    is_liked_by_user    = serializers.SerializerMethodField()
    is_disliked_by_user = serializers.SerializerMethodField()
    category            = DreamCategorySerializer(many=True, read_only=True)
# category
    class Meta:
        model = Dream
        fields = ['id',"category", 'title', 'description', 'thumbnail', 'created_at', 'likes_count', 'dislikes_count', 'is_liked_by_user', 'is_disliked_by_user', 'comments']

    def create(self, validated_data):
       categories          = validated_data.pop("category", None)
       categories_for_item = [] 
       obj = Dream.objects.create(**validated_data)
       if categories:
           for category in categories:
                try:
                   
                    obj_cate = DreamCategory.objects.get(pk=category.get("id")) 
                    categories_for_item.append(obj_cate)
                except:
                   pass

       obj.category.add(categories_for_item)

       return obj



    def get_likes_count(self, obj):
        return obj.dream_likes.count()

    def get_dislikes_count(self, obj):
        return obj.dream_dislikes.count()

    def get_is_liked_by_user(self, obj):
        user = self.context.get('request').user
        return obj.dream_likes.filter(user=user).exists()

    def get_is_disliked_by_user(self, obj):
        user = self.context.get('request').user
        return obj.dream_dislikes.filter(user=user).exists()
