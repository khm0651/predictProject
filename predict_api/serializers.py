from rest_framework import serializers
from .models import DailyPrice,CompanyInfo

class CompanyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyInfo
        fields = ('code','company','last_update') # 필드 설정


class DailyPriceSerializer(serializers.ModelSerializer):

    data = CompanyInfoSerializer(read_only = True)

    class Meta:
        model = DailyPrice
        fields = ('code','date','open','high','low','close','diff','volume','data') # 필드 설정
