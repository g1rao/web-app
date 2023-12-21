FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /gitstapi
COPY . .
RUN pip3 install -r requirements.txt
CMD /usr/bin/python3 app.py