FROM alpine
RUN apk update && apk upgrade && apk add --no-cache python3 py3-pip
FROM mysql
COPY . .
RUN pip install -r requirements.txt

