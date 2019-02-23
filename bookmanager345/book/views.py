from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
import json

from rest_framework.viewsets import ModelViewSet

from book.BookInfoSerializer import BookInfoSerializer
from book.models import BookInfo


def login_required(func_view):
    def wrapper(req, *args, **kwargs):
        if False:
            return func_view(req, *args, **kwargs)
        else:
           return  HttpResponse('login ok')
    return wrapper


def index(req):
    if req.method == 'GET':
        return HttpResponse('ok')
    else:
        return HttpResponse('This is post request')


def test_template(req):
    return render(req, 'test_template.html', context={
        'name': 'TEM'
    })


def get_books(req):
    books = BookInfo.objects.all();
    # books = list(books)
    datas = []
    for book in books:
        datas.append({
            'name': book.name,
            'pub_date': book.pub_date
        })

    return  JsonResponse(data={'data': datas}, safe=False)

def post_book(req):
    data = json.loads(req.body.decode())
    print('收到数据为')
    print(data)
    # 省略校验逻辑
    book = BookInfo.objects.create(
        name = data.get('name'),
        pub_date = data.get('pubdate')
    )
    return  JsonResponse(data={
        'id': book.id,
        'name': book.name,
         'pub_date': book.pub_date,
        'readcount': book.readcount

    }, status='201', safe=False )


def put_book(req, id):
    if req.method == 'PUT':
        try:
            book = BookInfo.objects.get(pk=id)
        except:
            return  HttpResponse(status=404)
        data = json.loads(req.body.decode())
        book.name = data.get('name')
        book.pub_date= data.get('pub_date')
        book.save()
        return  JsonResponse(data={
            'id': book.id,
            'name': book.name,
            'pub_date': book.pub_date,
            'readcount': book.readcount

        }, status='201', safe=False )


def del_book(req, id):
    if req.method == 'DELETE':
        try:
            book = BookInfo.objects.get(pk=id)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        book.delete()
        return HttpResponse('ok', status=204)



def get_books_rest(req):
    pass

def get_books_apiviw(req):
    pass


class BookInfoViewSet(ModelViewSet):
     queryset = BookInfo.objects.all()
     serializer_class = BookInfoSerializer

