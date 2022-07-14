from django.shortcuts import render
from rest_framework.views import APIView

from .serial import SOPTSeriailzer,tagsSeriailzer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .models import SpotInfo,CommentTag

# Create your views here.
class SPOTView(APIView):
    def get(self, request):
        MM = SpotInfo.objects.all()
        Sdetial = SOPTSeriailzer(instance=MM, many=True)
        json = JSONRenderer().render(Sdetial.data)
        return HttpResponse(json, content_type='application/json')

class tagsView(APIView):
    def get(self, request):
        MM = CommentTag.objects.all()
        Sdetial = tagsSeriailzer(instance=MM, many=True)
        json = JSONRenderer().render(Sdetial.data)
        return HttpResponse(json, content_type='application/json')
class buttonView(APIView):
    def get(self,request):
        m=SpotInfo.objects.values('poiId')
        #如需添加其他类，只需要在values里添加就可
        #m=SpotInfo.objects.values('poiId',"poiName","shortFeatures")
        for i in range(len(m)):
            num=m[i]['poiId']
            m[i]['url']=f'https://m.ctrip.com/webapp/you/comment/district/4229-11.html?openapp=5&poiId={num}'
        json = JSONRenderer().render(m)
        return HttpResponse(json, content_type='application/json')