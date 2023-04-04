from django.shortcuts import render

from django.http import HttpResponse
import requests, os,pytz,tzdata,datetime
from django.utils import timezone


from .models import Blog,Book,Author


def home(request):
    mytest=timezone.get_fixed_timezone(offset=5*60+30)
    ctx={
        'mytest':mytest
    }
    return render(context=ctx,template_name='core/home.html',request=request)

def edit(request):
    ctx={}
    return render(context=ctx,template_name='core/edit.html',request=request)

import time
def testops(request):
    ctx={}

    rr=str(int(time.time()))
    # res=Author.objects.create(name='mahs'+rr,profession='def')
    # res=Author.objects.get(id=9)
    # res.book_set.add(Book.objects.create(title='champak2'+rr))
    # ff=res.book_set.all()

    boo=Author.objects.filter(book__id=5)
    ff=boo
    print(ff)
    return HttpResponse(f"{ff}")
