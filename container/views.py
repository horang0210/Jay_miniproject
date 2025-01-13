from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ContainerSerializer
from .models import Containers
from rest_framework.response import Response
from rest_framework import status
import os
import re

class ContainerView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        try:
            container = Containers.objects.get(username=request.user)  # 외래키로 연결된 username 사용
            serializer = ContainerSerializer(container)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Containers.DoesNotExist:
            return Response({"message": "컨테이너가 존재하지 않습니다."}, status=status.HTTP_200_OK)


    def post(self, request):
        if Containers.objects.filter(username=request.user, is_created=True).exists():
            return Response({"message": "이미 컨테이너를 가지고 있습니다."}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'username': request.user.id,
            'container_name': request.user.username,  # container_name = username
            'is_created': False  
        }

        serializer = ContainerSerializer(data=data, context={'request': request})  # request 객체 전달
        if serializer.is_valid():
            serializer.save()

            container_name = str(request.user.username)
            container_name = re.sub(r'[^A-Za-z0-9_.]', '-', container_name)  # 영문, 숫자, _, . 외 문자는 하이픈(-)로 변환
            container_name = str.lower(container_name)  # 대문자는 소문자로 변환
            os.system(f'docker build . --build-arg USERNAME={container_name} -t {container_name}')
            os.system(f'docker run -itd --gpus all --name {container_name} {container_name}')   # container 생성 시 container_name = username
            
            serializer.instance.is_created = True
            serializer.instance.save()
            
            if serializer.instance.is_created == True:
                return Response({"message": "컨테이너가 생성되었습니다."}, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
