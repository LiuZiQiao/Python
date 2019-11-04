from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
    test1 = Test(name='lxk')
    test1.save()
    return HttpResponse('<p>数据添加成功</p>')