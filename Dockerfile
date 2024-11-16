FROM ubuntu:latest
LABEL authors="granth"

WORKDIR /flaskblog

ENTRYPOINT ["top", "-b"]

COPY requirements.txt .
RUN pip install --no-cache dir -r requirements.txt

COPY . .
EXPOSE 5000

ENV FLASK_APP=flaskblog.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]