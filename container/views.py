from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ContainerSerializer
from .models import Containers
from rest_framework.response import Response
from rest_framework import status

class ContainerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            container = Containers.objects.get(username=request.user)  # 외래키로 연결된 username 사용
            serializer = ContainerSerializer(container)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Containers.DoesNotExist:
            return Response({"message": "컨테이너가 존재하지 않습니다."}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        data = request.data
        data['username'] = request.user.id  # 현재 로그인한 사용자의 ID로 설정
        serializer = ContainerSerializer(data=data, context={'request': request})  # request 객체 전달
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

