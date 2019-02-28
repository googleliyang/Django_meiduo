- 是否验证频繁请求看下, 好像是这样的如果太多请求 何必再去走代码浪费性能，直接 RESPONSE(status) 多好
- 短信发送成功与否看下

- 跨域的话 get 请求可以到服务器Ok, post 请求会先发送预请求(预请求返回的结果既我支持你跨域的请求)

- 不用ViewSet 的话， 修改密码还要单独写一个 class吗，倒也不用 原先class 上加一个 put 方法即可



## ISSUE
- 为什么之前接口状态都是根据  data ， code: 而http 一律200

- logger 每次都要导入 设置不合理吧

- 存在 super().create 成功密码修改不成功的情况
- 存在写入成功读取数据失败的情况，但此时用户已经注册成功，这样则影响实际注册结果

- 服务器 jwt 生成的 token 字段不存储吗

- 为什么自己的 在 allow 字段多余的时候没有日志, 对比老师第三天节点看下, 以及日志 rest 捕获的异常 ？

- 对比 直接 200, 然后 code msg 的方式

- 如果将 allow 字段问题的 读取时模型上没有allow Attribute Error , rest 也没有捕获
     
     - 复现方式，将 自定义异常日志打印加入 类型判断
     - allow wirte only 去掉

## Tip

- 序列化过程就是 拿序列化器的字段一个个去 Model 上找。

- django 的 allow_hosts 相当于 Php laravel serve 的 0.0.0.0  原理就是 django 的这个 allow hosts(一种安全机制)

- serializer create .. update 返回的数据即 restful 返回的数据

```python
        # 如此在 创建成功后，也就是注册成功后会拿到 带有 token 的数据
        # token 是不存入数据库的，屙屎每次根据用户名密码生成
       jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
```

# 邮件验证流程

-> 接收邮件url
- 发送请求 绑定邮件
- 服务器收到请求绑定邮件到用户信息
- 服务器发送验证邮件 , 采用itsdanger 加密


-> 验证邮件 url, get 请求

- 服务器收到请求，解析出用户 id 和 绑定的邮件地址
- 如果与用户本身的邮件地址一样，修改 verified 为已验证

## 问题Serializer 写好之后，再遇到一个 提供一个自定义的 更新方式后，后边再遇到一个
与之前更新方式不同的更新方式，怎么办? 如用户已经有了 serializer 的 update又来一个保存邮件

自思考解决方式：
1. 不使用 serializer, 直接进行保存以及数据的返回, 但是进行数据验证就比较麻烦
2. 新写一个 serializer , 因为本来就会有多个不同的 serializer

## 问题; jwt 中获取 用户 信息, 但是三级视图默认不是 queryset 也就是 所有的需要传递 id 参数吗

- 一下逻辑太多未记地牢靠难免少了 权限 等诸如此类的很多东西


- 绑定邮件那里不必先查是否之前有绑定只需要 unique = True 即可




## Attension
- EMAIL_FROM: 要么邮箱地址，要么是 xxx<邮箱地址>, 否则发送不成功
- 自关联一对多就一张表

```python
| areas | CREATE TABLE `areas` (                                                                                  |
|       |   `id` int(11) NOT NULL AUTO_INCREMENT,                                                                 |
|       |   `name` varchar(10) NOT NULL,                                                                          |
|       |   `parent_id` int(11) DEFAULT NULL,                                                                     |
|       |   PRIMARY KEY (`id`),                                                                                   |
|       |   KEY `areas_parent_id_c913d672_fk_areas_id` (`parent_id`),                                             |
|       |   CONSTRAINT `areas_parent_id_c913d672_fk_areas_id` FOREIGN KEY (`parent_id`) REFERENCES `areas` (`id`) |
|       | ) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8
```

## ISSUE 

- 如同邮箱验证那里， itsdangerous 中验证失败服务器会停止，部署的时候 怎么解决这个问题

- 如下地方需要好好理解下

- 修改的话也是所有字段都必须传吗？ 使用 ModelViewSet 时， 有没有更好的方式

```python
需要使用related_name指明查询一个行政区划的所有下级行政区划时，使用哪种语法查询，如本模型类中指明通过Area模型类对象.subs查询所有下属行政区划，而不是使用Django默认的Area模型类对象.area_set语法。

没吊用，serializer 新起一个 字段也可以查，和 Meta 的 fields 中一致即可

```


- 赠：

所有的学习不熟悉，都将如用 vim 一般，急速茁壮成长起来
