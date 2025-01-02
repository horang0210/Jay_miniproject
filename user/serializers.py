from rest_framework import serializers
from .models import UserInfo


# 회원가입 Serializer
class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = UserInfo.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
        ) 
        
        user.save()
        return user
    
    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'password_check', 'name', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}, 'password_check': {'write_only': True}}
        
    # password과 password_check의 일치 여부 확인
    def validate(self, data): 
        if data['password'] != data['password_check']:
            raise serializers.ValidationError(
                {"password_check": "비밀번호와 일치하지 않습니다."})
        return data

    
# 사용자 정보 조회 Serializer
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserInfo
        fields = ['username', 'name', 'phone_number']
        queryset = UserInfo.objects.all()
        




