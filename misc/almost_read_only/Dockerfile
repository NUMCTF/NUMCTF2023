# docker build -t almost_read_only .
# docker run -p 10004:10004 almost_read_only:latest

FROM python:3.9-slim

WORKDIR /app

COPY . /app

EXPOSE 10004

CMD ["python", "service.py"]
