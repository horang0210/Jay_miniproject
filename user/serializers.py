from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth import authenticate
from django.forms import ValidationError

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
        

# # 로그인 Serializer
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Login Error")
        
        
        
# # 회원가입 Serializer
# class RegisterSerializer(serializers.ModelSerializer): 
#     class Meta:
#         model = UserInfo
#         fields = ['username', 'password', 'name', 'phone_number']
#         extra_kwargs = {'password':{'write_only':True}, 
#                         # 'name':{'write_only':True}, 
#                         # 'phone_number':{'write_only':True}, 
#                         }
#         queryset = UserInfo.objects.all()
        
#     # 사용자 정보 생성
#     def create(self, validated_data):
#         user = UserInfo.objects.create_user(
#             username=validated_data['username'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
        
#         # # 사용자의 토큰 생성
#         # token = Token.objects.create(user=user)
#         # print(token.key)
#         # return user


# # # 로그인 Serializer
# # class LoginSerializer(serializers.ModelSerializer):
    


# # class RegisterSerializer(serializers.ModelSerializer):
    
# #     # ID에 대한 중복 검증
# #     username = serializers.CharField(
# #         required=True,
# #         validators=[UniqueValidator(queryset=User.objects.all())], 
# #     )
    
# #     # 비밀번호에 대한 검증
# #     password = serializers.CharField(
# #         write_only=True,
# #         required=True,
# #         validators=[validate_password], 
# #     )
    
# #     # 비밀번호 확인 필드
# #     password_check = serializers.CharField( 
# #         write_only=True,
# #         required=True,
# #     )
    
# #     # 이름 필드
# #     name = serializers.CharField( 
# #         write_only=True,
# #         required=True,
# #     )
    
# #     # 전화번호 필드
# #     phone_number = serializers.CharField( 
# #         write_only=True,
# #         required=True,
# #     )

# #     class Meta:
# #         model = User
# #         fields = ('username', 'password', 'password_check', 'name', 'phone_number')

# #     # password과 password_check의 일치 여부 확인
# #     def validate(self, data): 
# #         if data['password'] != data['password_check']:
# #             raise serializers.ValidationError(
# #                 {"password": "Password fields didn't match."})
# #         return data


