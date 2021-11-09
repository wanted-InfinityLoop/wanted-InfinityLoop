FROM python:3 

ADD . /www 

WORKDIR /www 

RUN python3 -m pip install -U pip 

RUN pip install -r requirements.txt

CMD uwsgi uwsgi.ini



# FROM python:3.8

# WORKDIR /usr/src/app

# COPY requirements.txt ./

# RUN pip install -r requirements.txt

# COPY . .

# EXPOSE 80

# ENTRYPOINT [ "python" ]


# CMD [ "app.py" ]

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
# CMD ["python", "./app.py"]
# CMD ["gunicorn", "--preload"]
# CMD ["gunicorn :app", "--bind", "0.0.0.0:8000"]