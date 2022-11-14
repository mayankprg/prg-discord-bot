FROM python:3.10.6




COPY . /app
WORKDIR /app

RUN apk add  --no-cache ffmpeg

RUN pip install -r requirements.txt


CMD ["python3", "bot.py"]