# 编写业务逻辑
# 业务处理逻辑都在views.py文件里。


from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog import models

# Create your views here.

# 4、创建一个用户信息列表，预定义了两个数据，将它们返回给浏览器，展示给用户
# user_list = [
#     {'user': 'jack', 'pwd': '123'},
#     {'user': 'tom', 'pwd': '456'},
# ]

# 5、使用数据库保存数据。建立初始数据
models.UserInfo.objects.create(user='Jack', pwd='1230')
models.UserInfo.objects.create(user='Tom', pwd='4560')


# request 参数必须有，名字是类似self的默认规则，可以改。它封装了用户请求的所有内容。
def index(request):
    # request.POST
    # request.GET
    if request.method == 'POST':
        # 3、获取用户输入。获得用户输入的用户名和密码
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)

        # 分别处理登录成功和登录失败，跳转到不同的界面
        if username == 'sdc' and password == '123456':
            # 4、传递数据。可以传递字符串或者列表，在html中循环遍历列表，列表中需要是字典
            # render方法接收第三个参数，是后台返回给浏览器的数据，它是一个字典，data是你自定义的指针名字，他会被对应的html文件引用
            # return render(request, 'login_success.html', {'user': username, 'pwd': password})
            # temp = {'user': username, 'pwd': password}
            # user_list.append(temp)

            # 5、使用数据库保存数据。添加数据到数据库中
            models.UserInfo.objects.create(user=username, pwd=password)
            # 5、从数据库读取所有数据
            user_list = models.UserInfo.objects.all()
            return render(request, 'login_success.html', {'user': username, 'data': user_list})
        else:
            return render(request, 'login_failure.html')
    else:
        # 1、返回字符串。不能直接返回字符串，必须是由这个类封装起来，这是django的规则，不是python的
        # return HttpResponse('Hello, blog !')
        # 2、返回html文件。当你想返回一个html文件时，就要用render方法来渲染（其实就是打包的意思）。render是django提供的方法和规则，就是这个用法
        # 第一个参数是固定的，第二个参数指定要返回的html文件
        return render(request, 'index.html')
