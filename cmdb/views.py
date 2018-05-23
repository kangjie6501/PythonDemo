from django.shortcuts import render
from django.shortcuts import HttpResponse

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
        temp = {"user":username,"pwd":password}
        user_list.append(temp)
        print(username,password)
    return render(request,"index.html",{"data":user_list})