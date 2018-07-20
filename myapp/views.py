from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("这个是一个测试Django")
    return render(request,"test.html")