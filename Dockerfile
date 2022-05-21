FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /backend_test
COPY requirements.txt /backend_test/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /backend_test/

