FROM python:3
WORKDIR /app
COPY ./API.py /app
RUN pip install prometheus_client
CMD [ "python", "./API.py" ]
EXPOSE 8000/tcp