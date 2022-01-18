FROM python:3

WORKDIR /usr/db_games

COPY ./webapp/. .
RUN pip install -r requirements.txt

EXPOSE 5000

COPY ./webapp/. .


CMD [ "python", "app.py" ]


 
