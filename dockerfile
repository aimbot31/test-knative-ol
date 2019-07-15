FROM python:buster

ENV FLASK_APP=app.py

EXPOSE 8080

RUN pip install flask requests

COPY ./app.py ./app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]