FROM alpine:latest
RUN apk update && apk add stress-ng bash
COPY stress-script.sh /usr/local/bin/stress-script.sh
RUN chmod +x /usr/local/bin/stress-script.sh
ENTRYPOINT ["/usr/local/bin/stress-script.sh"]