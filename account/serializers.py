from rest_framework import serializers
from account.models import AccountModel

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = '__all__'