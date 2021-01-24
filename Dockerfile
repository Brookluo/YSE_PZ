FROM centos:7

EXPOSE 8000

# python and basic softwares
RUN yum install -y \
    epel-release \
    gcc \
    git \
    openssl bzip2 libffi zlib \
    libpython3.6-dev \
    python3-devel \
    curl \
    wget && \
    yum clean all

RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py

# install yse_pz
RUN git clone https://github.com/Brookluo/YSE_PZ.git && \
    cd YSE_PZ && \
    pip3 install numpy && \
    pip3 install -r requirements.txt
