# Use an official Python runtime as a parent image
FROM python:3.6.5-slim-stretch

ARG USER=flatspace

RUN mkdir -p /home/$USER

RUN groupadd -r $USER \
    && useradd -r -g $USER -d /home/$USER  -s /sbin/nologin -c "Docker image user" $USER


COPY ./requirements /opt/requirements

RUN apt-get update && \
    apt-get install -y curl gcc g++ && \
    apt-get clean && \
    apt-get purge && \
    pip install --upgrade pip

ARG ENV=prod

RUN pip install -r /opt/requirements/$ENV.txt

ARG APP_DIR=/opt/skinner
COPY . $APP_DIR
RUN chown -R $user:$user $APP_DIR

USER $user

WORKDIR $APP_DIR
