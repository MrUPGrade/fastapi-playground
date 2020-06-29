FROM python:3.7

WORKDIR /src
ENV PYTHONPATH /src

ADD requirements.txt /src/requirements.txt
ADD api /src/api

RUN pip  install --no-cache --upgrade pip && pip install --no-cache -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "api.app:app"]
