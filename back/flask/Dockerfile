FROM python:3
RUN mkdir /marvel_tmi
WORKDIR /marvel_tmi
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . . 
CMD ["uwsgi", "uwsgi.ini"]
