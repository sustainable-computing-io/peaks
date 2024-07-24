FROM python:3.12
WORKDIR /workspace
COPY read_prom.py /workspace
COPY metrics.properties /workspace
COPY requirements.txt /workspace
RUN pip install -r requirements.txt
RUN ["mkdir", "data"]
CMD ["python3", "read_prom.py"]