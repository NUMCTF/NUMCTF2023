# sudo docker build -t pie .
# sudo docker run -p 10000:10000 pie:latest

FROM ubuntu:22.04

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt install gcc xinetd make cowsay -y

COPY xinetd.conf /etc/xinetd.d/ctf
COPY Makefile /src
COPY ./flag.txt /
COPY ./pie.c /src
COPY run.sh /src

RUN make

RUN chmod 444 /flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash", "/src/run.sh"]
EXPOSE 10000