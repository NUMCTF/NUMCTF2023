# sudo docker build -t myagmartseren/numctf:pie .
# sudo docker run -p 10000:10000 myagmartseren/numctf:pie
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat dash
EXPOSE 10000

RUN useradd -m ctf
COPY pie /home/ctf/
COPY flag.txt /home/ctf/
WORKDIR /home/ctf

RUN chmod 444 /home/ctf/flag.txt

USER ctf
CMD ["socat", "tcp-l:10000,reuseaddr,fork", "EXEC:./pie"]