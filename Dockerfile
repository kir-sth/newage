FROM python:3.12

COPY bot.py config_reader.py db.py requirements.txt /workdir/
COPY /filters/ /workdir/filters/
COPY /handlers/ /workdir/handlers/
COPY /keyboards/ /workdir/keyboards/

WORKDIR /workdir

RUN pip install -r requirements.txt

CMD ["python", "./bot.py"]
