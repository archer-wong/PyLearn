## 1 安装

#### 1.1 安装pip
    wget https://bootstrap.pypa.io/get-pip.py  
    python get-pip.py

#### 1.2 安装django  
    pip install django==1.10.6

## 2 创建项目
#### 2.1 使用 管理工具 django-admin.py 来创建 PyLearn 项目：
    django-admin.py startproject PyLearn
```
# root @ VM_33_19_centos in /data/PyLearn [10:21:21] 
$ tree
.
|-- manage.py
`-- PyLearn
    |-- __init__.py
    |-- settings.py
    |-- urls.py
    `-- wsgi.py

1 directory, 5 files
```
- manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
- PyLearn/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
- PyLearn/settings.py: 该 Django 项目的设置/配置。
- PyLearn/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
- PyLearn/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

#### 2.2 启动服务
    python manage.py runserver 0.0.0.0:8000
    
问题：

```
$ /usr/local/bin/python manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).
July 05, 2017 - 07:48:51
Django version 1.11.3, using settings 'helloworld.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
Invalid HTTP_HOST header: '123.206.102.238:8000'. You may need to add u'123.206.102.238' to ALLOWED_HOSTS.
[05/Jul/2017 07:48:58] "GET / HTTP/1.1" 400 61159
Invalid HTTP_HOST header: '123.206.102.238:8000'. You may need to add u'123.206.102.238' to ALLOWED_HOSTS.
[05/Jul/2017 07:48:58] "GET /favicon.ico HTTP/1.1" 400 61108
^\[1]    4615 quit (core dumped)  /usr/local/bin/python manage.py runserver 0.0.0.0:8000
```
去创建的项目中修改 setting.py 文件：
ALLOWED_HOSTS = ['*']   ＃在这里请求的host添加了＊

- 在浏览器输入你服务器的ip及端口号，如果正常启动，输出结果如下：
```
It worked!
Congratulations on your first Django-powered page.
```

### 本文章以下所有列子组织结构

[实例基本来自于菜鸟教程](http://www.runoob.com/django/django-tutorial.html)

为了方便学习代码上传，[github地址](https://github.com/archer-wong/PyLearn)
```
# root @ VM_33_19_centos in /data/PyLearn [15:11:27] 
$ tree
.
|-- db.sqlite3
|-- manage.py
|-- PyLearn
|   |-- form.py
|   |-- form.pyc
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- settings.py
|   |-- settings.pyc
|   |-- urls.py
|   |-- urls.pyc
|   |-- viewdb.py
|   |-- viewdb.pyc
|   |-- view.py
|   |-- view.pyc
|   |-- wsgi.py
|   `-- wsgi.pyc
|-- templates
|   |-- base.html
|   |-- children.html
|   |-- get_form.html
|   |-- hello.html
|   `-- post_form.html
`-- TestModel
    |-- admin.py
    |-- admin.pyc
    |-- apps.py
    |-- __init__.py
    |-- __init__.pyc
    |-- migrations
    |   |-- 0001_initial.py
    |   |-- 0001_initial.pyc
    |   |-- __init__.py
    |   `-- __init__.pyc
    |-- models.py
    |-- models.pyc
    |-- tests.py
    `-- views.py

4 directories, 34 files

```

## 3 编程实例

以下是一个完整的（路由--控制器--视图）实例

路由文件:urls.py

```
from django.conf.urls import url 
from . import view

urlpatterns = [ 
    url(r'^$', view.hello),
]

```

控制器:view.py

```
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
```

视图文件:hello.html

    <h1>{{ hello }}</h1>

配置文件：settings.py

```
TEMPLATES = [ 
    {   
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates"],  //绑定视图文件位置
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],  
        },  
    },  
]
```

## 4 Django 模板标签

###### 1 if标签
基本用法  
```
{% if condition %}
     ... display
{% endif %}
```

或者：
```
{% if condition1 %}
   ... display 1
{% elif condition2 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}
```

{% if %} 标签接受 and ， or 或者 not 关键字来对多个变量做判断 ，或者对变量取反（ not )，例如：
```
{% if athlete_list and coach_list %}
     athletes 和 coaches 变量都是可用的。
{% endif %}
```

###### 2 for 标签
```
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```

给标签增加一个 reversed 使得该列表被反向迭代：
```
{% for athlete in athlete_list reversed %}
...
{% endfor %}
```

可以嵌套使用 {% for %} 标签：
```
{% for athlete in athlete_list %}
    <h1>{{ athlete.name }}</h1>
    <ul>
    {% for sport in athlete.sports_played %}
        <li>{{ sport }}</li>
    {% endfor %}
    </ul>
{% endfor %}
```
###### 3 ifequal/ifnotequal 标签

{% ifequal %} 标签比较两个值，当他们相等时，显示在 {% ifequal %} 和 {% endifequal %} 之中所有的值。

下面的例子比较两个模板变量 user 和 currentuser :
```
{% ifequal user currentuser %}
    <h1>Welcome!</h1>
{% endifequal %}
```
和 {% if %} 类似， {% ifequal %} 支持可选的 {% else%} 标签：8
```
{% ifequal section 'sitenews' %}
    <h1>Site News</h1>
{% else %}
    <h1>No News Here</h1>
{% endifequal %}
```

###### 4 过滤器

模板过滤器可以在变量被显示前修改它，过滤器使用管道字符，如下所示：

    {{ name|lower }}

{{ name }} 变量被过滤器 lower 处理后，文档大写转换文本为小写。

过滤管道可以被* 套接* ，既是说，一个过滤器管道的输出又可以作为下一个管道的输入：

    {{ my_list|first|upper }}

以上实例将第一个元素并将其转化为大写。

有些过滤器有参数。 过滤器的参数跟随冒号之后并且总是以双引号包含。 例如：

    {{ bio|truncatewords:"30" }}

这个将显示变量 bio 的前30个词。

###### 5 include 标签

{% include %} 标签允许在模板中包含其它的模板的内容。

下面这个例子都包含了 nav.html 模板：

    {% include "nav.html" %}

###### 6 模板继承

接下来我们先创建之前项目的 templates 目录中添加 base.html 文件，代码如下：
templates/base.html 文件代码：
```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>base</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>base.html 段落base。</p>
    {% block mainbody %}
       <p>base.html 内容base</p>
    {% endblock %}
</body>
</html>
```
以上代码中，名为 mainbody 的 block 标签是可以被继承者们替换掉的部分。


hello.html 中继承 base.html，并替换特定 block，hello.html 修改后的代码如下：
templates/hello.html 文件代码：
```
{% extends "base.html" %}
 
{% block mainbody %}
    <p>children.html 内容children</p>
{% endblock %}
```

重新访问地址 http://127.0.0.1:8000/hello，输出结果如下：
```
Hello World!

base.html 段落base。

children.html 内容children
```

## 5 数据模型

#### 5.1 安装mysql数据驱动 
    pip install mysqlclient

我这里报错 mysql_config: command not found  
解决方法是  

    yum install mysql-devel
```
Installed:
  MariaDB-devel.x86_64 0:10.0.20-1.el7.centos
Complete!
```
【注】因为我安装的是MariaDB所以这里是MariaDB-devel

#### 5.2 数据库配置

settings.py: 文件代码：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'pylearn',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```
这里添加了中文注释，所以你需要在 HelloWorld/settings.py 文件头部添加 # encoding: utf-8

#### 5.3 定义模型

Django规定，如果要使用模型，必须要创建一个app。

    django-admin.py startapp TestModel
    
目录结构如下：
```
.
|-- db.sqlite3
|-- manage.py
|-- PyLearn
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- settings.py
|-- templates
|   |-- base.html
|   |-- children.html
|   `-- hello.html
`-- TestModel
    |-- admin.py
    |-- admin.pyc
    |-- apps.py

```

TestModel/models.py: 文件代码：
```
# models.py
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)
```

以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。

接下来在settings.py中找到INSTALLED_APPS这一项，如下：

```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestModel',     # 添加此项
)
```

在命令行中运行：
```
python manage.py migrate   # 创建表结构

$ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate TestModel   # 创建表结构
看到几行 "Creating table…" 的字样，你的数据表就创建好了。
Creating tables ...
……
Creating table TestModel_test  #我们自定义的表
……
```

- 表名组成结构为：应用名_类名（如：TestModel_test）。
- 注意：尽管我们没有在models给表设置主键，但是Django会自动添加一个id作为主键。

#### 5.4 数据库操作

##### 1- 添加数据
urls.py

```
from django.conf.urls import url                                            
from . import view
from . import viewdb  #  新文件

urlpatterns = [                                                                   
    url(r'^$', view.hello),
    url(r'^test/$', view.test),
    url(r'^testdb/$', viewdb.testdb), # 新路由                              
]

```

viewdb.py

```
$ vim viewdb.py

# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test

def testdb(request):
    test1 = Test(name='archer')
    test1.save()
    return HttpResponse('<p>添加数据成功</p>')

```

##### 2- 获取数据

Django提供了多种方式来获取数据库的内容，如下代码所示：

testdb.py: 文件代码：
```
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    # 初始化
    response = ""
    response1 = ""
    
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1) 
    
    # 获取单个对象
    response3 = Test.objects.get(id=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]
    
    #数据排序
    Test.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
```


##### 3- 更新数据

修改数据可以使用 save() 或 update():

testdb.py: 文件代码：
```
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse("<p>修改成功</p>")
```
##### 4- 删除数据

删除数据库中的对象只需调用该对象的delete()方法即可： 

testdb.py: 文件代码：
```
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()
    
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    
    # 删除所有数据
    # Test.objects.all().delete()
    
    return HttpResponse("<p>删除成功</p>")
```

## 6 表单

urls.py

```
from django.conf.urls import url 
from . import view
from . import viewdb
from . import form

urlpatterns = [ 
    url(r'^$', view.hello),
    url(r'^test/$', view.test),
    url(r'^testdb/$', viewdb.testdb),
    url(r'^get-form/$', form.get_form),
    url(r'^submit-get/$', form.submit_get),
    url(r'^post-form/$', form.post_form),
    url(r'^submit-post/$', form.submit_post),
]


```
form.py

```
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf

def get_form(request):
    return render(request, 'get_form.html')

def submit_get(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q'].encode("utf-8")
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

def post_form(request):
    return render(request, 'post_form.html')

def submit_post(request):
    ctx ={} 
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post_form.html", ctx)

```

get_form.html

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>get 表单</title>
    </head>
    <body>
        <form action="/submit-get" method="get">
            <input type="text" name="q">
            <input type="submit" value="搜索">
        </form>
    </body>
</html>
```

post_form.html

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>post 表单</title>
    </head>
    <body>
        <form action="/submit-post/" method="post">
            {% csrf_token %}
            <input type="text" name="q">
            <input type="submit" value="Submit">
        </form>
        <p>{{ rlt }}</p>
    </body>
</html>

```
    
**提交post表单的时候报错**

RuntimeError: You called this URL via POST, but the URL doesn’t end in a slash and you have APPEND_SLASH set.

提示form的action地址最后不是/结尾的，而且APPEND_SLASH的值是Ture

将from的action地址改为/结尾的就可以了  
或者  
修改settings:APPEND_SLASH=False
