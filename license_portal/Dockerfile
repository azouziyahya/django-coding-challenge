FROM python:3.10
ENV WAIT_VERSION 2.7.2

RUN mkdir -p /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY entrypoint.sh /app/
WORKDIR /app
EXPOSE 8080

RUN chmod +x entrypoint.sh
ENTRYPOINT ["bash","/app/entrypoint.sh"]