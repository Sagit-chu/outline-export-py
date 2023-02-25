FROM python:slim
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev
VOLUME [ "/data" ]
COPY outline-export.py /app
WORKDIR /app
RUN pip install pipreqs \
    pipreqs .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "outline-export.py" ]