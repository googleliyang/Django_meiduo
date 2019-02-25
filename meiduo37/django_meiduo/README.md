- 是否验证频繁请求看下, 好像是这样的如果太多请求 何必再去走代码浪费性能，直接 RESPONSE(status) 多好
- 短信发送成功与否看下

- 跨域的话 get 请求可以到服务器Ok, post 请求会先发送预请求(预请求返回的结果既我支持你跨域的请求)


## ISSUE
- 为什么之前接口状态都是根据  data ， code: 而http 一律200

- 存在 super().create 成功密码修改不成功的情况
- 存在写入成功读取数据失败的情况，但此时用户已经注册成功，这样则影响实际注册结果

- 服务器 jwt 生成的 token 字段不存储吗

## Tip

- django 的 allow_hosts 相当于 Php laravel serve 的 0.0.0.0  原理就是 django 的这个 allow hosts(一种安全机制)