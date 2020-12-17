FROM python:3.8-alpine3.11

RUN apk add --update --no-cache \
    python3-dev \
    build-base \
    linux-headers

WORKDIR /src
COPY setup.sh /src
RUN chmod +x *.sh && ./setup.sh

RUN apk del \
    python3-dev \
    build-base \
    linux-headers

COPY . /src
RUN rm -rf .git
