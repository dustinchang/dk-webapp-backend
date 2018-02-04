# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from dk_webapp_api.settings import DEBUG
from rest_framework import viewsets, status
from rest_framework.response import Response
if DEBUG:
    from account_service import AccountService
else:
    from apps.users.account_service import AccountService

if DEBUG:
    from serializers import AccountSerializers
else:
    from apps.users.serializers import AccountSerializers

class AccountViewSet(viewsets.GenericViewSet):
    serializer_class = AccountSerializers
    account_service = AccountService()

    def retrieve(self, request, pk=None):
        account = self.account_service.retrive_account(pk)
        serializer = self.serializer_class(account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_account = self.account_service.create_account(request.data)
        serializer = self.serializer_class(new_account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)