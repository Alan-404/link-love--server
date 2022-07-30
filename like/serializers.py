from rest_framework import serializers
from like.models import LikeModel

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = "__all__"