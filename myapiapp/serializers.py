from django.contrib.auth.models import User
from rest_framework import serializers
from myapiapp.models import *

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ('id', 'username', 'first_name', 'last_name', 'email')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMaster
        fields = ('id','eventName','place','time','duration','cast','categoryName')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMaster
        fields = ('id','categoryName','parentName') 