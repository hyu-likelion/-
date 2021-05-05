from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Todolist
# Create your views here.

@csrf_exempt
def select(request):
    data = Todolist.objects.all()
    ret = []
    for i in data:
        ret.append([i.mainText, i.created_at, i.is_approve])
    ret = json.dumps(ret)
    return HttpResponse(ret, status=200)

def update(request):
    data = Todolist.objects.get(match_id=request.POST['id'])
    data.update(is_approve= not data.is_approve)
    return HttpResponse("성공", status=200)

def delete(request):
    data = Todolist.objects.get(match_id=request.POST['id'])
    data.delete()
    return HttpResponse("성공", status=200)

def insert(request):
    data = Todolist.objects.create(mainText=request.POST['mainText'])
    return HttpResponse("성공", status=200)

