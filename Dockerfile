FROM python:3-alpine as prereqs

RUN mkdir -p /opt/app
COPY ./source/ /opt/app/
WORKDIR /opt/app/

COPY ./requirements.txt /opt/app/requirements.txt
RUN pip3 install --no-python-version-warning --no-cache-dir -r requirements.txt
RUN rm requirements.txt

ENTRYPOINT [ "python3", "-m", "docker_entry" ]