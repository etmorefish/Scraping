from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    # return HttpResponse("Hello Django!")
    return render(request, 'baidu.html')