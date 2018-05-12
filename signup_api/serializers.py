from rest_framework import serializers
from .models import Test_form
from rest_framework.response import Response
from rest_framework import status

class Test_formSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test_form
        fields = ("first_name", "last_name", "email", "password")

class Validate_formSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255,required=True)
    password = serializers.CharField(max_length=128,required=True)
