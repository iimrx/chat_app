FROM alpine
RUN apt-get update -y && apt-get upgrade -y && apt-get dist-upgrade && apt-get autoremove

COPY . .
RUN pip install -r requirements.txt
