# Flask笔记

## 快速入门
1. 外网访问
    ```
	app.run(host='0.0.0.0')
	```
2. 路由参数转换器
	* int
	* float
	* path
3. 	url规则

	```python
@app.route('/projects/')
def projects():
　　return 'The project page'
@app.route('/about')
def about():
　　return 'The about page'
```

	>虽然它们看起来着实相似，但它们结尾斜线的使用在 URL 定义 中不同。 第一种情况中，指向 projects 的规范 URL 尾端有一个斜线。这种感觉 很像在文件系统中的文件夹。访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范 URL 去。

	>然而，第二种情况的 URL 结尾不带斜线，类似 UNIX-like 系统下的文件的 路径名。访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误。

	>这个行为使得在遗忘尾斜线时，允许关联的 URL 接任工作，与 Apache 和其它的服务器的行为并无二异。此外，也保证了 URL 的唯一，有助于 避免搜索引擎索引同一个页面两次。

4. 模板默认传入对象
	* requset、session和g
	* get\_flashed\_messages()函数
	* config

5. 	关于用户上传文件名
	>永远不要信任filename

	`from werkzeug import secure_filename`

6. 存储cookie

	```
	from flask import make_response
	@app.route('/')
	def index():
    resp = make_response(render_template(...))
    	resp.set_cookie('username', 'the 	username')
    	return resp
	```

7. 定制错误
	* abort 弹出错误
	* @bp.errorhandler
	* 全局 @error_bp.app_errorhandler

8. 响应

	>1. 如果返回的是一个合法的响应对象，它会从视图直接返回。
	2. 如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建。
	3. 如果返回的是一个元组，且元组中的元素可以提供额外的信息。这样的元组必须是 **(response, status, headers)** 的形式，且至少包含一 个元素。 status 值会覆盖状态代码， headers 可以是一个列表或 字典，作为额外的消息标头值。
	4. 如果上述条件均不满足， Flask 会假设返回值是一个合法的 WSGI 应用 程序，并转换为一个请求对象。

9. 会话

	>除请求对象之外，还有一个 session 对象。它允许你在不 同请求间存储特定用户的信息。它是在 Cookies 的基础上实现的，并且对 Cookies 进行密钥签名。

10. flash()

	* get\_flashed\_messages()函数


11. logger

	>```
	app.logger.debug('A value for debugging')
	app.logger.warning('A warning occurred (%d apples)', 42)
	app.logger.error('An error occurred')
	```

## request对象
1. request.method

	请求方法
2. 	request.args

	url参数
3. 	request.files

	文件

4. 	request.cookies
