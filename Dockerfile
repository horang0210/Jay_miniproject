#$USERNAME mini project v2: Dockerfile 작성
#Ubuntu 20.04 & CUDA 11.8 & cuDNN 8.6.0 & NCCL 2.15.5 & Anaconda latest 

#기본 이미지 지정
FROM ubuntu:20.04

#docker build 중에 프롬프트(라이센스 동의, 경고) 무시
ENV DEBIAN_FRONTEND=noninteractive 

#날짜&시간을 한국 서울 기준으로 변경
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#필요한 apt 패키지 설치(불필요한 패키지 설치 X, 버전 다운그레이드 허용, 고정 버전 패키지에서 다른 버전 설치 허용)
RUN apt update && apt install -y --no-install-recommends --allow-downgrades --allow-change-held-packages \
    curl \
    vim \
    nano \
    apt-utils \
    ca-certificates \
    sudo \
    git \
    make \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

#CUDA 설치(container 안에는 nvidia-driver를 설치하지 않는데, cuda로 설치하면 nvidia-driver가 함께 설치되므로 cuda-toolkit을 설치)
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    apt update && apt install -y cuda-toolkit-11-8 

#cuDNN, NCCL 패키지 설치
RUN apt update && apt install -y --no-install-recommends --allow-downgrades --allow-change-held-packages \
    libcudnn8=8.6.0.163-1+cuda11.8 \
    libcudnn8-dev=8.6.0.163-1+cuda11.8 \
    libnccl2=2.15.5-1+cuda11.8 \
    libnccl-dev=2.15.5-1+cuda11.8 \
    && rm -rf /var/lib/apt/lists/*
 
ENV PATH="/usr/local/cuda-11.8/bin${PATH:+:${PATH}}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"


# 컨테이너 빌드 시 사용자 이름을 받을 변수 정의
ARG USERNAME
# ARG PASSWORD
ENV USERNAME=${USERNAME}
ENV HOME=/home/${USERNAME}

# 컨테이너 내부에 사용자 홈 디렉토리 생성
RUN useradd -m -s /bin/bash $USERNAME && \
    # echo "$USERNAME:$PASSWORD" | chpasswd && \
    usermod -aG sudo $USERNAME

# 사용자 로그인 후 작업 홈 디렉토리 설정
USER $USERNAME
WORKDIR $HOME

#사용자 홈 디렉토리에 anaconda 패키지 설치(최신 버전)
RUN wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh -O $HOME/anaconda.sh && \
    bash $HOME/anaconda.sh -b -p $HOME/anaconda && \
    rm $HOME/anaconda.sh && \
    $HOME/anaconda/bin/conda init

#anaconda의 bin 디렉토리를 PATH에 추가
ENV PATH="$HOME/anaconda/bin:$PATH"

#사용자 홈 디렉토리 안에 Docker container 실행할 디렉토리 생성
RUN mkdir $HOME/workspace

#Docker container에서 명령 실행될 디렉토리로 선언
WORKDIR $HOME/workspace

#gpu-burn(GPU 부하테스트용) 설치
RUN git clone https://github.com/wilicc/gpu-burn && \
    cd gpu-burn && \
    make && \
    cd ..

