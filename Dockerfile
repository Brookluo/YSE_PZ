FROM centos:7

# python and basic softwares
RUN yum install -y \
    epel-release \
    gcc \
    git \
    openssl bzip2 libffi zlib \
    libpython3.6-dev \
    python3-devel \
    mysql-devel \
    curl \
    wget && \
    yum clean all

RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py

RUN mkdir /usr/src/yse

WORKDIR /usr/src/yse

# install yse_pz
RUN git clone https://github.com/Brookluo/YSE_PZ.git

WORKDIR /usr/src/yse/YSE_PZ    
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD YSE_PZ/settings.ini ./YSE_PZ

EXPOSE 8000

# CMD [ "python3", "manage.py", "migrate" ]
# ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]