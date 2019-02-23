from django.db import DatabaseError
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from book.models import PeopleInfo
from .people_serializer import PeopleSerializer


class PeopleInfoMix(GenericAPIView, ListModelMixin, CreateModelMixin):

    queryset = PeopleInfo.objects.all()
    serializer_class = PeopleSerializer
    filter_fields = ['id','name']

    def get(self, req):

        raise DatabaseError('error')
        return self.list(req)

    def post(self, req):
        return self.create(req)


class PeopleInfoDetailMix(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):

    queryset = PeopleInfo.objects.all()
    serializer_class = PeopleSerializer

    def get(self, req, pk):
        return self.retrieve(req)

    def put(self, req, pk):
        return self.update(req)

    def delete(self, req, pk):
        return self.destroy(req)
