from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ContainerSerializer
from .models import Containers
from rest_framework.response import Response
from rest_framework import status
import os

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
        if Containers.objects.filter(username=request.user).exists():
            return Response({"message": "이미 컨테이너를 가지고 있습니다."}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'username': request.user.id,
            'container_name': request.user.username,  # container_name = username
            'is_created': True  
        }

        serializer = ContainerSerializer(data=data, context={'request': request})  # request 객체 전달
        if serializer.is_valid():
            serializer.save()

            os.system('docker build . --build-arg USERNAME='+str(request.user.username)+' -t '+str(request.user.username))
            os.system('docker run -itd --gpus all '+str(request.user.username))

            return Response({"message": "컨테이너가 생성되었습니다."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
