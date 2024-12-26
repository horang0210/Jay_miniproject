from rest_framework import serializers
from .models import Containers
from django.core.exceptions import ValidationError

class ContainerSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True)  # username을 읽기 전용으로 설정

    class Meta:
        model = Containers
        fields = ['container_name', 'is_created', 'username']

    def validate(self, data):
        request = self.context.get('request')  # request 객체 가져오기
        if not request:
            raise serializers.ValidationError("Request 객체가 필요합니다.")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        return Containers.objects.create(username=user, **validated_data)
