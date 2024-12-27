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
        data = request.data
        data['username'] = request.user.id  # 현재 로그인한 사용자의 ID로 설정
        serializer = ContainerSerializer(data=data, context={'request': request})  # request 객체 전달
        if serializer.is_valid():
            serializer.save()   
            # 사용자에 맞는 container 생성 및 실행
            if serializer.data['is_created'] is True:   
                os.system('docker build . --build-arg USERNAME='+str(request.user)+' -t '+str(data['container_name']))
                # os.system('docker rename Jay_image' + data['username'])   # 이미 빌드된 이미지를 username으로 이름 변경
                os.system('docker run -itd --gpus all '+ str(data['container_name']))
                return Response("컨테이너가 생성되었습니다.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

