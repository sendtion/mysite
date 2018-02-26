from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

# request 参数必须有，名字是类似self的默认规则，可以改。它封装了用户请求的所有内容。
def index(request):
    return HttpResponse('Hello, polls !')
