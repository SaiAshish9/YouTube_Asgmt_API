FROM python:3.8.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /youtube_videos

WORKDIR /youtube_videos

ADD . /youtube_videos/

RUN python3 -m pip install -r requirements.txt
