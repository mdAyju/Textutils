from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def base(request):
    b=request.POST.get('check','off')
    a=request.POST.get('txt')
    upper=request.POST.get('upper','off')
    line= request.POST.get('line','off')
    space=request.POST.get('space','off')
    count= request.POST.get('count','off')
    res=''
    punc='''!@#$%^&*()_+}{:"><?|\-;'=.,}'''
    if b=='on':
        
        for i in a:
            if i not in punc:
                res+=i
        anything={'first':'ONE','finial':res}
        a=res
        # return render(request,'base.html',anything)
    if upper=='on':
        res=''
        for i in a:
            res+=i.upper()
        anything={'first':'ONE','finial':res}
        a=res
    if line=='on':
        res=''
        for i in a:
            if not(i=='\n') and not(i=='\r'):
                res+=i
        anything={'first':'removed line','finial':res}
        a=res
    if space=='on':
        res=''
        for i,j in enumerate(a):
            if not(a[i]==' ' and a[i+1]==' '):
                res+=j
        anything={'first':'removed','finial':res}
        a=res
    if count=='on':
        total= a.split()
        res=len(total)
        anything={'first':'count','finial':res}
    return render(request,'base.html',anything)

