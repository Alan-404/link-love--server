from bson import is_valid
from account.models import AccountModel
from account.serializers import AccountSerializer
from django.contrib.auth.hashers import make_password, check_password
from bson.objectid import ObjectId
class AccountService:
    def add_account(self, user):
        user['password'] = make_password(user['password'])
        account_serializer = AccountSerializer(data=user)
        if account_serializer.is_valid():
            account_serializer.save()
            return user
        return None

    def get_account_by_user_id(self, user_id):
        account = AccountModel.objects.get(user_id = user_id)
        account_serializer = AccountSerializer(account)
        return account_serializer.data

    def check_password_account(self, password, hashed_password):
        if check_password(password, hashed_password):
            return True
        return False


    def change_password(self, account_id,  old_password, new_password):
        account = AccountModel.objects.get(_id=ObjectId(account_id))
        if account is None:
            return False
        if self.check_password_account(old_password, account.password) == False:
            return False
        account_data = account.__dict__
        account_data['password'] = make_password(new_password)
        account_serializer = AccountSerializer(account, data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return True
        return False

    def get_account_by_id(self, id):
        account = AccountModel.objects.get(_id=ObjectId(id))
        account_serializer = AccountSerializer(account)
        return account_serializer.data
    
        

