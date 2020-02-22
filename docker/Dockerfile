FROM python:3.7.6
LABEL maintainer="isPlaying"

ADD api /web/api
WORKDIR /web/api
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt
EXPOSE 10001
CMD python run.py