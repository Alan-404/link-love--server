from like.serializers import LikeSerializer

class LikeService:
    def add_like(self, like_data):
        like_serializer = LikeSerializer(like_data)
        if like_serializer.is_valid():
            like_serializer.save()
            return like_serializer.data
        return None