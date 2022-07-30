from post.serializers import PostSerializer
from post.models import PostModel
from datetime import datetime

class PostService:
    def add_post(self, post):
        post['created_at'] = datetime.now()
        post['modified_at'] = datetime.now()
        post_serializer = PostSerializer(data=post)
        if post_serializer.is_valid():
            post_serializer.save()
            return post_serializer.data
        return None

    def get_all(self):
        posts = PostModel.objects.all()
        posts_serialzier = PostSerializer(posts, many=True)
        return posts_serialzier.data

    def like_post(self, post_id):
        post = PostModel.objects.get(_id=post_id)
        if post is None:
            return None
        post_data = post.__dict__
        post_data['likes'] += 1
        post_serializer = PostSerializer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return post_serializer.data
        return None
