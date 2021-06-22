FROM alpine
RUN apk update && apk upgrade && apk add py3-pip

COPY . .
RUN pip install -r requirements.txt
