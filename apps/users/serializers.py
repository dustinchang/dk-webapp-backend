from rest_framework import serializers
from models import Account

class AccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'name',
            'email',
            'phone_number'
        )