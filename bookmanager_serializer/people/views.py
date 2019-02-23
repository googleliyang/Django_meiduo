import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import View, APIView

from book.models import PeopleInfo
from .people_serializer import PeopleSerializer

from rest_framework.response import Response

## TODO:1 类视图正常写法
class PeopleInfoView(View):

    filter_fields = ['id','name']

    def get(self, req):
        peoples = PeopleInfo.objects.all()
        # 对比两次 debug 讲解
        #问题1：  step into, 对比 step into mycode
        #问题2：  Step PeopleSerializer step over 不执行 init 吗
        #问题3: 进入后执行 Dispatch
        # 感觉并没有 通过 debug 看到了代码 一步一步 的完整执行过程
        # serializer = PeopleSerializer(instance=peoples, many=True)
        # data into
        people_list = []
        for people in peoples:
            people_list.append({
                'name': people.name,
                 'id': people.id,
                 'book_name': people.book.name,
                 'description': people.description,
                  # gender 在不使用序列化器的时候 返回 0，1 使用序列化器的时候 返回 男 女
                 'gender': people.gender
            })

        # return Response(data=serializer.data)
        return JsonResponse(data=people_list, safe=False)

    def post(self, request):
        # 获取数据
        json_str = request.body
        json_str = json_str.decode()  # python3.6 无需执行此步
        req_dict = req_data = json.loads(json_str)
        print(req_data)
        # serializer = PeopleSerializer(data=req_data)
        # serializer.save()
        people = PeopleInfo.objects.create(
            name=req_data.get('name'),
            book_id=req_data.get('book')
        )
        return JsonResponse({
            'name': people.name,
            'pub_date': people.id
        }, safe=False)
        # return HttpResponse(req_dict.get('name'))
        #


# 参数是正则命名匹配传过去的
class PeopleInfoDetail(View):

    def get(self, req, id):
        try:
            people = PeopleInfo.objects.get(pk=id)
        except PeopleInfo.DoesNotExist:
            # 返回这里柑橘不好
            return HttpResponse(status=400)
        return JsonResponse({
            'name': people.name,
             'id': people.id
        }, safe=False)

    def put(self, req, id):
        try:
            people = PeopleInfo.objects.get(pk=id)
        except PeopleInfo.DoesNotExist:
            return HttpResponse(status=400)
        params = json.loads(req.body.decode())
        name = params.get('name', people.name)
        people.name = name
        people.save()
        return JsonResponse({
            'name': people.name,
             'id': people.id,
             'description': people.description,
            'gender': people.gender
        }, status=200)

    def delete(self, req, id):
        try:
            people = PeopleInfo.objects.get(pk=id)
        except PeopleInfo.DoesNotExist:
            return HttpResponse(status=400)
        people.delete()
        # return JsonResponse(data='ok', status=204)
        return HttpResponse(status=204)



