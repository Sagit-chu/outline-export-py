FROM python
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev
COPY outline-export.py /
VOLUME [ "/data" ]
ENTRYPOINT [ "python", "outline-export.py" ]