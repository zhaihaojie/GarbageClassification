from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from garbage_classfication import settings
import os
import json
from .baiduapi import text_classify, picture
# 导入,可以使此次请求忽略csrf校验
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index/welcome.html')


@csrf_exempt
def receive_img(request):
    '''服务器'''
    '''获取POST到服务器的文件对象'''
    if request.method == "POST":
        files = request.FILES
        '''
         需要通过小程序端的key（image）获取二进制数据
         获取文件内容
        '''
        content = files.get('image', None).read()
    '''
    设置保存路径
        settings.IMAGES_DIR 已经默认设定
        默认保存文件名字为aaa.jpg
    '''
    path = os.path.join(settings.IMAGES_DIR, '1.jpg')
    with open(path, 'wb') as f:
        f.write(content)
        '''保存图片到本地'''
    result = picture.get_result(path)
    return HttpResponse(json.dumps(result))


@csrf_exempt
def text(request):
    if request.method == 'POST':
        data = request.body.decode()
        gbname = json.loads(data)['gbname']
        gbclass = text_classify.get_gbclass(gbname)

    return HttpResponse(gbclass)
