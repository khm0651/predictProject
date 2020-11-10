from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DailyPrice,CompanyInfo
from .serializers import DailyPriceSerializer,CompanyInfoSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def stocklist(request):
    if request.method == 'GET':
        # query_set = CompanyInfo.objects.all()
        # serializer = CompanyInfoSerializer(query_set, many=True)
        query_set = DailyPrice.objects.filter(date=request.GET['date'])
        serializer = DailyPriceSerializer(query_set, many=True)

        return JsonResponse(serializer.data, safe=False)
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = ClosingPriceSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

