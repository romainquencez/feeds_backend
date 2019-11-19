FROM python:3.8

# Set environment variables
# PYTHONDONTWRITEBYTECODE means Python won’t try to write .pyc files which we also do not desire.
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED ensures our console output looks familiar and is not buffered by Docker, which we don’t want.
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    gcc \
    graphviz \
    graphviz-dev \
    libmemcached-dev \
    libpq-dev \
    openssh-client \
    vim \
    && apt-get autoremove -y \
    && apt-get clean -y

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements*.txt /app/
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
RUN pip install -r requirements-tests.txt
