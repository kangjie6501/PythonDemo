from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.
#https://blog.csdn.net/Sunshine_ZCC/article/details/73918408
user_list=[
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},
]
def index(request):
 #   return HttpResponse("hello world!")
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=password)
    user_list = models.UserInfo.objects.all()
        #temp = {"user":username,"pwd":password}
        #user_list.append(temp)
        #print(username,password)
    return render(request,"index.html",{"data":user_list})