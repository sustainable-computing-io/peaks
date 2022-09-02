FROM debian:stretch-slim

WORKDIR /

COPY cmd/peaks /usr/local/bin

CMD ["peaks"]