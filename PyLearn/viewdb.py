# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test

def testdb(request):
    test1 = Test(name='archer')
    test1.save()
    return HttpResponse('<p>添加数据成功</p>')

