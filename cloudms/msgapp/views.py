from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(resquest):
    datalist = []
    if resquest.method == "POST":
        userA = resquest.POST.get("userA", None)
        userB = resquest.POST.get("userB", None)
        msg = datetime.now()
        with open('msgdata.txt', 'a+')  as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA, msg, datetime.strftime("%Y-%m-%d %H:%M:%S")))

    if resquest.method == "GET":

        userC = resquest.GET.get("userC", None)
        if userC != None:
            with open('msgdata.txt', 'r') as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA":linedata[1], "msg":linedata[2], "time":linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return render(resquest, 'index.html' ,{"data":datalist})

