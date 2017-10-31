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
