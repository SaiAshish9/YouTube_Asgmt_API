FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /youtube_videos

WORKDIR /youtube_videos

ADD . /youtube_videos/

RUN pip install -r requirements.txt
