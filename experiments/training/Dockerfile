FROM python:3.12
WORKDIR /workspace
ENV FLASK_APP=read_prom.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PROMETHEUS='http://prometheus:9090'
ENV STORAGEPATH='/mnt/data/storage'
COPY read_prom.py /workspace
COPY metrics.properties /workspace
COPY requirements.txt /workspace
RUN pip install -r requirements.txt
EXPOSE 5000