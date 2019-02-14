from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse

from book.models import BookInfo
from django.db import connection


def index(request):
    data = list(BookInfo.objects.all())
    # return HttpResponse('ok')
    # print(data)
    print(connection.queries)
    context = {'books': data}
    return render(request, 'account.html')
    # return HttpResponse('okk')


def lazy(req, name, id):
    print('id is %s, name is %s' % (id, name))
    books = BookInfo.objects.all()
    # just run once time
    # for i in books:
    #     print(i)
    # for i in books:
    #     print(i)
    # for i in books:
    #     print(i)
    # return render(req, 'account.html')
    return HttpResponse('ok')


def query(request):
    """get param"""
    print('query string name is', request.GET.get('name'))
    print('query string pass is', request.GET.get('pass'))
    print('query string pass is', request.GET.getlist('name'))
    print('Think url is =', reverse('book:query'))
    return HttpResponse('ok')

