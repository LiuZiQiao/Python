from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from dianying import models
# Create your views here.

def index(request):
        return render(request, 'index.html')


def person(request):
        return render(request,'person.html')



def register(request):
    if request.method == 'GET':
        print("requset.method post ,register")
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        re_pwd = request.POST.get('re_pwd')
        if name and pwd and re_pwd:
            if pwd == re_pwd:
                user_obj = models.User.objects.filter(uname=name).first()
                if user_obj:
                    return HttpResponse('用户已存在')
                else:
                    models.User.objects.create(uname=name, upasswd=pwd).save()
                    return redirect('/login/')
            else:
                return HttpResponse('两次密码不一致')

        else:
            return HttpResponse('不能有空！')


def login(request):
    # request这是前端请求发来的请求，携带的所有数据，django给我们做了一些列的处理，封装成一个对象传过来
    # 其实挺简单，学会用它给你的一些方法就好了，其实你自己也想到它是怎样处理的。
    if request.method == 'GET':
        return render(request, 'account/login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user_obj = models.User.objects.filter(uname=name, upasswd=pwd).first()
        if user_obj:
            return render(request, 'index.html')
        else:
            return HttpResponse('用户名或密码错误')


# def register(request):
#     if request.method == 'GET':
#         return render(request,'register.html')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         pwd = request.POST.get('pwd')
#         re_pwd = request.POST.get('re_pwd')
#         if name and pwd and re_pwd:
#             if pwd == re_pwd:
#                 user_obj = models.User.objects.filter(name=name).first()
#                 if user_obj:
#                     return HttpResponse('用户已存在')
#                 else:
#                     models.User.objects.create(name=name,pwd=pwd).save()
#                     return redirect('/login/')
#             else:
#                 return HttpResponse('两次密码不一致')
#
#         else:
#             return HttpResponse('不能有空！')