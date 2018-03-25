# Use an official Python runtime as a parent image
FROM python:3.6.1-slim as skinner

ARG ENV=prod
ARG USER=flatspace
ARG APP_DIR=/opt/skinner

RUN mkdir -p /home/$USER

RUN groupadd -r $USER \
    && useradd -r -g $USER -d /home/$USER  -s /sbin/nologin -c "Docker image user" $USER


COPY ./requirements /opt/requirements

RUN apt-get update && \
    apt-get install -y curl gcc g++ && \
    apt-get clean && \
    apt-get purge && \
    pip install --upgrade pip && \
    pip install -r /opt/requirements/$ENV.txt

COPY . $APP_DIR

RUN chown -R $user:$user $APP_DIR

USER $user

WORKDIR $APP_DIR

#RUN pip install .

EXPOSE 5000

WORKDIR $APP_DIR/skinner

CMD ["python", "skinner.py"]
