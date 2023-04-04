from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView


from .serlzs import AuthSerl, BSerl, BooSerl


from core.models import Blog,Book,Author

class test(APIView):

    def get(self,request):
        qs=Blog.objects.all()
        resp=BSerl(qs,many=True)
        return Response({
            'blogs':resp.data
        })

class bookv(APIView):

    def get(self,request):
        qs=Book.objects.all()
        resp=BooSerl(qs,many=True)
        return Response({
            'books':resp.data
        })

class authorv(APIView):
    
    def get(self,request):
        qs=Author.objects.all()
        resp=AuthSerl(qs,many=True)
        return Response({
            'authors':resp.data
        })
