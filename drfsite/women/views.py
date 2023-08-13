from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class WomenAPIView(APIView):
    def get(self, request):
        list_women = Women.objects.all()
        
        return Response({
            'posts': WomenSerializer(list_women, many=True).data
        })
        
    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'post': serializer.data
        })

    def put(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({
                'error': 'Method put not allowed!'
            })
        
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Object does not exists!'
            })
            
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'post': serializer.data
        })
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({
                'error':
                    'Method delete not allowed!'
                })
            
        women = Women.objects.get(pk=pk)
        women.delete()
            
        return Response({
            'post': 'delete post ' + str(pk)
        })