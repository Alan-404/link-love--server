
from user.models import UserModel
from user.serializers import UserSerializer
from bson.objectid import ObjectId
from datetime import datetime

class UserService:
    def get_all_users(self):
        users = UserModel.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return users_serializer.data

    def add_user(self, user):
        user['created_at'] = datetime.now()
        user['modified_at'] = datetime.now()
        user_serializer = UserSerializer(data=user)
        if user_serializer.is_valid():
            user_serializer.save()
            user['user_id'] = user_serializer['_id'].value
            return user
        return None

    def get_user_by_email(self, email):
        user = UserModel.objects.get(email=email)
        user_serializer = UserSerializer(user)
        return user_serializer.data

    def get_user_by_id(self, id):
        user = UserModel.objects.get(_id=ObjectId(id))
        user_serializer = UserSerializer(user)
        return user_serializer.data