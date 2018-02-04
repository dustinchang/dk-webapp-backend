from apps.users.models import Account

class AccountService():

    def retrive_account(self, pk):
        # Should catch for exceptions
        return Account.objects.get(id=pk)

    def create_account(self, data):
        new_account = Account(name=data.get('name'), email=data.get('email') , phone_number=data.get('phone_number'))
        new_account.save()
        return new_account
