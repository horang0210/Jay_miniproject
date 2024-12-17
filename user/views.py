from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout, authenticate
from .serializers import RegisterSerializer, UserSerializer
# from django.contrib.auth.views import LogoutView
from .models import UserInfo

# 회원가입 View
class RegisterView(CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer
    
    
# 사용자 세부 사항 View
class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    
# 로그아웃 View
class LogoutView(APIView):
    """
    Djano 5 does not have GET logout route anymore, so Django Rest Framework UI can't log out.
    This is a workaround until Django Rest Framework implements POST logout.
    Details: https://github.com/encode/django-rest-framework/issues/9206
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({'message' : '로그아웃 완료'})
    
# class PatchLogoutView(LogoutView):
#     http_method_names = ["get", "post", "options"]

#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)


# # 로그인 View
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         # 사용자 인증
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)  # 세션 생성
#             return Response({"message": "로그인 완료"})
#         else:
#             return Response({"error": "잘못된 접근으로 다시 확인해주세요."})

# # 로그아웃 View
# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]  # 인증된 사용자 확인

#     def post(self, request):
#         logout(request)  # 세션 삭제
#         return Response({"message": "로그아웃 완료"})



# class RegisterView(CreateAPIView):
#     queryset = UserInfo.objects.all()
#     serializer_class = RegisterSerializer

# # 로그인 View
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return Response({"message": "로그인 완료"})
#         return Response({"error": "올바른 계정 정보가 아닙니다."})

# # 로그아웃 View
# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({"message": "로그아웃 완료"})
    






