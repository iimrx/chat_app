FROM alpine, ngnix
RUN apt-get update -y && apt-get upgrade -y && apt-get dist-upgrade && apt-get autoremove
