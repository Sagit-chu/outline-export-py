FROM python:slim
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev
VOLUME [ "/data" ]
WORKDIR /app
COPY outline-export.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "outline-export.py" ]