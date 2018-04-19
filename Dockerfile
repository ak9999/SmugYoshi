FROM python:3.6-stretch
ADD ./app /app
WORKDIR /app

ARG DISCORD_TOKEN

RUN pip install -r requirements.txt
RUN python3 yoshi.py
