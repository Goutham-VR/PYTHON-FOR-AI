from django.shortcuts import render

# Create your views here.
# Throttling
# Throttling controls how many API requests a user/client can make within a certain time.
# add DEFAULT_THROTTLE_RATES in settings.py
#=========================================================================================
# 1. AnonRateThrottle limits requests from unauthenticated users.
#=========================================================================================
# works with APIView/GenericAPIView/ConcreteGenericAPIView
# APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle # import for throttle

class ThrottlingApiView(APIView):
    throttle_classes=[AnonRateThrottle] # calling throttle classes
    def get(self,request):
        return Response({
            'message':'Throttling API Working'
        })

# if authenticated limitless req can do otherwise req/min rate this is defined in settings

# GenericAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from apiview.models import Product
from apiview.serializers import ProductSerializer

class ThrottlingGenericApiView(ListModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer
    throttle_classes = [AnonRateThrottle]
    def get(self,request):
        return self.list(request)

# ConcreteGenericAPIView
from rest_framework.generics import ListAPIView

class ThrottlingConcreteGenericApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer
    throttle_classes = [AnonRateThrottle]
