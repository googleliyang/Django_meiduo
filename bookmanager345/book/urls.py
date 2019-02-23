from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from book.BookView import BookView
from . import views

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'books', views.BookInfoViewSet, base_name='')  # 向路由器中注册视图集

urlpatterns = [
    # todo1: If demo must end with '/', 以及什么时候 有这个 / 感觉不是很清楚
        # ou called this URL via PUT, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining PUT data. Change your form to point to localhost:9000/peoples/1/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings
        # django 在put update post 默认需要加 / 结尾可以通过配置  APPEND_SLASH = False 解决
        # 不然 访问  localhost:9000/peoples/1 报错, 加了之后
        # 生成的路由依旧是 peoples/(?P<pk>[^/.]+)/$I 所以还是要 / 结尾只是之前的那个错误没有了
    # todo2: where define template & static
    # todo3: admin column & ...
    # todo4: if not register app, I never see the error
    # name = models.CharField(max_length=10) the useful of max_length compare to mysql
        # 会限制  django admin 可输入字段长度, mysql 设置varchar 会截取 字段长度(只截取 varchar 设置的长度，不是可变的吗)，刚测试, 看看之前笔记并对比测试下
         # | name                 |
        # +----------------------+
        # | 123456789009876543wq
    # the useful of model __str__
    # name = models.CharField(max_length=10, verbose_name='名称') this verbose_name useful
    # func(*args, **keywards)
    # remember orm operation!! write &  remember, exact exclude q , f, __contains__.... __起头的

    # todo:// 补一个增删改查的写法
    # 正常写每个方法对应一个请求，不使用类视图的情况下，需要每个方法写一个路由，或者一个方法中判断四种请求方式很不方便
        # 使用类视图后，get 和 post 写一种请求方式，详情，修改删除，写一种，定义两个路由即可

    # 图片显示问题
    ## 超媒体url 以及 restful 的使用

    # defaultUrl post method must end with / ? & compare simple..
    #
    # ! 数据传输所有格式 以及接收格式记忆.

    # bookinfoAdmin 管理类无印象
    # 通过设置short_description属性，可以设置在admin站点中显示的列名。无印象 检查原因， 看是否为第三天上午， 不是为何

    # 问老师那个 github 的动态url 怎么体现的实际开发中又是怎么用的

    # 改manager.py 点击run让他可以运行那里

    # remember
    # QuerySet，表示从数据库中获取的对象集合
    # url(r'^books$', views.BookInfoViewSet),
    url(r'^', include(router.urls)),
    # url(r'^index/$', views.index),
    # # url(r'^class/$', BookView.as_view()),
    # url(r'^tem/$', views.test_template),
    # url(r'^books/$', views.get_books),
    # url(r'^bookss/$', views.post_book),
    # url(r'^books/+$', views.post_book),
    # url(r'^ubooks/(?P<id>\d+)$', views.put_book),
    # url(r'^dbooks/(?P<id>\d+)$', views.del_book),

    # 今上午老师返回  count 的那个 response用的是? from rest_framework.response import Response?
        # 序列化器里必须定义所有字段吗 继承自 serilizalize 时需要，继承自 ModelSeriliaze 时不需要, demo 就是拿 model Serialize 来写的
    #     id = serializers.IntegerField(label='ID', read_only=True), label 作用
        # 老师说 label 如同 verbose 在api 文档中显示 在这我们可以暂时不用管它
        # 一个简短的文本字符串，可用作HTML表单字段或其他描述性元素中字段的名称。
            #     name = serializers.CharField(label='名字', max_length=20) 和 vebsore model的字段名同? 是的，label 即verbose
            # 那为什么嗨呀写呢(根据ModelViewSerializer 自动生成的测试的)
    #  serializer 里 定义的 max_length 长度和 model 不一样会怎么样, 检查有没有讲，还有serializer 只写部分字段
]
    # 那个像 github url 组的地址怎么出来的来着?
    # class PeopleSerialize(serializers.Serializer):
#     id = serializers.IntegerField(label='ID', read_only=True)
#     name = serializers.CharField(label='name', max_length=10)
    # 这里设置的 id, name serializer.data 查询出来的也是只要这两个字段，那么？modelSerialize 有什么用 也就是filed=[]
        # 答： 其实这两个并不冲突，自己写 serialize 后 就没法用 modelSerialize了！

    # serialize.date 如何返回也就是 httpResponse 和 Response 的使用

    #     book = BookInfoSerializer(), 关联查出对象，就像 laravel hali 返回的数据

    # 使用 apiview 的好处

        # 自动 根据 请求头响应?
        #
        # 支持定义的属性：
         # authentication_classes列表或元祖，身份认证类
        # permissoin_classes列表或元祖，权限检查类
        # throttle_classes列表或元祖，流量控制类
         # 在APIView中仍以常规的类视图定义方法来实现get() 、post() 或者其他请求方式的方法。

    # """
    # [
	# {
	# 	"id": 1,
	# 	"name": "郭靖",
	# 	"book": {
	# 		"id": 1,
	# 		"name": "python入门10",
	# 		"pub_date": "1990-05-01",
	# 		"readcount": 12,
	# 		"commentcount": 34,
	# 		"is_delete": false,
	# 		"image": null
	# 	}
	# },
    # """


    # 当在一对象上定义时，     peopleinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 新增
    # 需要加 many=True 参数
    # 最后再看一遍文档

    # srialize apiview 对比 generic view 对比  List..mix ..

        # Request 是 drf 改了 还是apiview 改了
     # REST framework 传入视图的request对象不再是Django默认的HttpRequest对象，而是REST framework提供的扩展了HttpRequest类的Request类的对象。
    #
        # REST framework 提供了Parser解析器，在接收到请求后会自动根据Content-Type指明的请求数据类型（如JSON、表单等）将请求数据进行parse解析，解析为类字典对象保存到Request对象中。

    # 选 modelSeriliaze 一定要有

    # orm 关系记忆
    # 再思考为什么这么设计，为何是这种关系
    # xmind 总结打印
    ## redis 取到的数据时 byte 需要转码后 再  lower() == text.lower()

    ## 1 get 代码中自动帮我们加了  / 结束 ， 2 hymedia api 使用只是给开发人员看的? 验证到github
    ## 3 使用到了 model 就必须注册 Installed app 否则报错 试一下
            # 草 是imodels.py !! 不是 用到了 Model
           # 是的 RuntimeError: Model class book.models.BookInfo doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.

    ## 开发过程中都是用 debug?

    ## 5：35 有队列的然后重启了 ？？效果走神了
    # 338 要结束 lable 是视图高级接口文档??
    # 5：07 worker 最后一点。。。到那个图
    # 5:47 不用些 url 的原因
    # 559 添加到 filed 里的原因再听一下把

    # 两个 meta 的区别 serializer 与 Model 中的 meta
        # serializer 中的 class Meta 和 admin 绝对没关系，只是在  api 响应与请求处调用
        # meodel 中的 是为 后台显示的

    # 从表外键必须填 老师没讲把, 也就是 people Info book, 讲的book
    # 以及 注释 csrf 后不能使用 页面提交了， 除非使用

    ## 代码赶一下吧 5000...
