FROM alpine
RUN apk update && apk upgrade && apk add --no-cache python3 py3-pip

COPY . .
RUN pip install -r requirements.txt
