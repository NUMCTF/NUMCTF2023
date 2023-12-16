# sudo docker build -t myagmartseren/numctf:overfusion .
# sudo docker run -p 10001:10001 myagmartseren/numctf:overfusion
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat dash
EXPOSE 10001

RUN useradd -m ctf
COPY overfusion /home/ctf/
COPY flag.txt /home/ctf/
WORKDIR /home/ctf

RUN chmod 444 /home/ctf/flag.txt

USER ctf
CMD ["socat", "tcp-l:10001,reuseaddr,fork", "EXEC:./overfusion"]