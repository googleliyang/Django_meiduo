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
