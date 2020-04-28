from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from api import serializers
from api.permissions import IsAdminOrOwner, IsAdminOrModeratorOrOwner


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializert
    pagination_class = PageNumberPagination
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ('list', 'create'):
            permission_classes = (IsAuthenticated, IsAdminUser, )
        elif self.action in ('retrieve', 'update', 'partial_update', 'destroy'):
            permission_classes = (IsAuthenticated,  IsAdminOrOwner)
        return [permission() for permission in permission_classes]


    def retrieve(self, request, username=None):
        if username == 'me':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        return super().retrieve(request, username)

    def partial_update(self, request, username=None, *args, **kwargs):
        if username == 'me':
            user = request.user
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, username=None, *args, **kwargs):
        if username == 'me':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)