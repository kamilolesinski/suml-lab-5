FROM python:3.12

WORKDIR /app

RUN apt-get update -y \
    && apt-get install -y python3-dev apt-utils build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade setuptools
RUN pip3 install cython==3.0.6 numpy==1.26.0

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

CMD gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT