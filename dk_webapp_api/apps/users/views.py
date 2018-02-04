# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from models import Account
from serializers import AccountSerializers
from account_service import AccountService

# Create your views here.
class AccountViewSet(viewsets.GenericViewSet):
    serializer_class = AccountSerializers
    account_service = AccountService()

    def retrieve(self, request, pk=None):
        account = self.account_service.retrive_account(pk)
        serializer = self.serializer_class(account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    #@list_route(methods=['post'])
    def create(self, request):
        new_account = self.account_service.create_account(request.data)
        serializer = self.serializer_class(new_account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)