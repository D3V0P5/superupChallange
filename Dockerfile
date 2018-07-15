FROM python:3.7.0-alpine3.7
#ADD . /code
WORKDIR /usr/src/app
COPY ./app/* ./
RUN pip install --no-cache-dir -r requirements

#RUN pip install -r ./requirements
#EXPOSE 5000
CMD ["python", "index.py"]
