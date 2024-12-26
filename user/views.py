from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout, authenticate
from .serializers import RegisterSerializer, UserSerializer
from .models import UserInfo

# 회원가입 View
class RegisterView(CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer
    
    
# 사용자 세부 사항 View
class DetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# 로그인 View
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 세션 생성
            return Response({"message": "로그인 완료"}, status=200)
        else:
            return Response({"error": "잘못된 접근으로 다시 확인해주세요."}, status=403)

        
# 로그아웃 View
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({'message' : '로그아웃 완료'}, status=200)






