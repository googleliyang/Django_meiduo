from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet

from book.models import BookInfo, PeopleInfo
from people_serialize.people_serialize import PeopleSerialize, PeopleViewSerializer
from book.BSerializer import BSerializer


class _PeopleInfo(View):

    def get(self, req, id):
        people = PeopleInfo.objects.get(pk=id)
        serialize = PeopleSerialize(instance=people, many=False)
        return JsonResponse(data=serialize.data, safe=False)
        # return HttpResponse('123')
    #
    # def get(self, req):
    #     books = BookInfo.objects.all()
    #     serialize = BSerializer(instance=books, many=True)
    #     return JsonResponse(data=serialize.data, safe=False)


class PeopleViewSet(ModelViewSet):
    queryset = PeopleInfo.objects.all()
    serializer_class = PeopleViewSerializer
    # serializer_class = PeopleSerialize

