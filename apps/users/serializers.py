from rest_framework import serializers
from dk_webapp_api.settings import DEBUG
if DEBUG:
    from models import Account
else:
    from apps.users.models import Account

class AccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'name',
            'email',
            'phone_number'
        )