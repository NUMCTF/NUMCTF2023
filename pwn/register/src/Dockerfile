# docker build -t register .   
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat dash
EXPOSE 10002

RUN useradd -m ctf
COPY register /home/ctf/
COPY flag.txt /home/ctf/
WORKDIR /home/ctf

USER ctf
CMD ["socat", "tcp-l:10002,reuseaddr,fork", "EXEC:./register"]