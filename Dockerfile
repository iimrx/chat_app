FROM alpine
RUN wget http://security.ubuntu.com/ubuntu/pool/main/a/apt/apt_1.0.1ubuntu2.17_amd64.deb -O apt.deb
RUN dpkg -i apt.deb
RUN apt-get update -y && apt-get upgrade -y && apt-get dist-upgrade && apt-get autoremove

COPY . .
RUN pip install -r requirements.txt
